import bcrypt


def hash_password(password: str):
    """Hash a password using bcrypt"""
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password


def verify_password(plain_password: str, hashed_password: str):
    """Check if the provided password matches the stored password"""
    password_byte_enc = plain_password.encode("utf-8")
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password)
