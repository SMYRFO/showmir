
from authx import AuthXConfig, AuthX
from app.config import settings

JWT_config = AuthXConfig()
JWT_config.JWT_SECRET_KEY = settings.SECRET_KEY
JWT_config.JWT_ALGORITHM = "HS256"
JWT_config.JWT_ACCESS_COOKIE_NAME = "access_token"
JWT_config.JWT_ACCESS_TOKEN_EXPIRES = None
JWT_config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=JWT_config)



