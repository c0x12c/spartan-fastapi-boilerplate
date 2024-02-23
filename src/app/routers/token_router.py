from fastapi import APIRouter, status, HTTPException, Depends
from src.app.schemas.token import TokenResponse, TokenRequest
from src.app.schemas.user import UserResponse
from src.service_layer import unit_of_work, services
from src.domain import model


token_router = APIRouter(prefix="/tokens", tags=["Tokens"])


@token_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse,
)
def new_token(token_request: TokenRequest):
    try:
        token, user_dict = services.create_token(
            email=token_request.email,
            password=token_request.password,
            uow=unit_of_work.SqlAlchemyUnitOfWork(),
        )
        return TokenResponse(user=UserResponse(**user_dict), token=token)
    except services.InvalidEmail as e:
        raise HTTPException(status_code=401, detail=str(e))
    except services.InvalidPassword as e:
        raise HTTPException(status_code=401, detail=str(e))
