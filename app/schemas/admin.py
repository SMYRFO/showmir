from pydantic import BaseModel

class Base(BaseModel):
    pass

class CreateAdmin(Base):
    token: str
    role: str
