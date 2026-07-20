from fastapi import APIRouter
from sqlalchemy import select
from app.database.database import SessionDep
from app.database.models import User_Model
router = APIRouter(
    prefix="/users",
    tags=["Users"] 
)

@router.get("/{user_id}")
async def get_user(user_id: int, session: SessionDep):
    query = select(User_Model).where(User_Model.id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    if user:
        return {"user_id": user_id, "balance": user.balance}
    else:
        return {"error": "User not found"}
