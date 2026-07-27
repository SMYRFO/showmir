from fastapi import APIRouter
from sqlalchemy import select
from app.database.database import SessionDep
from app.database.models import User_Model
from random import randint



router = APIRouter(
    prefix="/tests",
    tags=["Tests"]
)




@router.post("/fill_db_random_values")
async def fill_db_random_values(count: int, session: SessionDep): 
    try:
        for i in range(count):
            new_user = User_Model(balance=randint(0, 100))
            session.add(new_user)
        await session.commit()
        return {"ok": "True", "message": "Random users add successfully"} 
    except Exception as e:
        return {"ok": "False", "message": e} 