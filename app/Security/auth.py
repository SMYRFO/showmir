from fastapi import Request, HTTPException, status
import jwt
from app.Security.JWT_config import JWT_config

def get_current_admin_role(request: Request) -> str:
    token = request.cookies.get(JWT_config.JWT_ACCESS_COOKIE_NAME)
    if not token:
        return "1" # тут надо подумать что сделать 
    try:
        payload: dict = jwt.decode(token, str(JWT_config.JWT_SECRET_KEY), algorithms=[JWT_config.JWT_ALGORITHM])

        role_value = payload.get("role")
        if not isinstance(role_value, str):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Некорректный токен: отсутствует роль"
            )
        role: str = role_value
        return role

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Невалидный или просроченный токен"
        )
    
def get_current_admin_uid(request: Request) -> int:
    token = request.cookies.get(JWT_config.JWT_ACCESS_COOKIE_NAME)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Вы не авторизованы"
        )
    try:
        payload: dict = jwt.decode(token, str(JWT_config.JWT_SECRET_KEY), algorithms=[JWT_config.JWT_ALGORITHM])
        
        uid_value = int(payload.get("sub", 1))
        if not isinstance(uid_value, int):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Некорректный токен: отсутствует uid"
            )
        uid: int = uid_value
        return uid

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Невалидный или просроченный токен"
        )