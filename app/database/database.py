
from fastapi import Depends
from typing import Annotated

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy import  text
from app.config import settings

engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=False
)


new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

