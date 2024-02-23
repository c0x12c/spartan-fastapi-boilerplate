from datetime import datetime, timedelta
from typing import Dict
from jose import JWTError, jwt
from src.config import Config


def encode_jwt(data: Dict, expiry: timedelta = timedelta(minutes=60)):
    """Generate access token"""
    payload = data.copy()
    expire_in = datetime.utcnow() + expiry
    payload.update({"exp": expire_in})
    return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
