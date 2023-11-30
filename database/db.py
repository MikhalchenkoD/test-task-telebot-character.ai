from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("postgresql+asyncpg://postgres:1234@localhost/character")
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)