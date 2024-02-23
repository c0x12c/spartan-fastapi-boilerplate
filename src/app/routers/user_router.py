from fastapi import APIRouter, status, HTTPException, Depends
from src.app.schemas.user import UserResponse, UserRequest

from src.service_layer import unit_of_work, services
from src.domain import model


user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
def new_user(user_request: UserRequest):
    try:
        user = model.User.create(user_request.model_dump())
        user_dict = services.add_user(
            user=user, uow=unit_of_work.SqlAlchemyUnitOfWork()
        )
        return UserResponse(**user_dict)
    except services.InvalidEmail as e:
        raise HTTPException(status_code=409, detail=str(e))
