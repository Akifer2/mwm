from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine
)
from sqlalchemy.orm import DeclarativeBase
import os, dotenv

dotenv.load_dotenv()
engine = create_async_engine(os.getenv("DATABASE_URL"), echo=False, future=True)
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, expire_on_commit=False
)

class Base(DeclarativeBase):
    pass
