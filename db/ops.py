
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column, Integer, String, ForeignKey,
    select
)
from config_reader import config
from .models import User, WebLink


Base = declarative_base()

async def build_engine():
    return create_async_engine(config.database_url, echo=True)

async def get_session_maker(engine):
    return async_sessionmaker(engine, expire_on_commit=False)


async def user_exists(chat_id, session_maker) -> bool:
    async with session_maker() as session:
        stmt = select(User).where(User.chat_id == chat_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


async def create_user(chat_id, user_name, password, session_maker) -> None:
    async with session_maker()  as session:
        new_user = User(chat_id=chat_id, name=user_name, password=password)
        session.add(new_user)
        await session.commit()
