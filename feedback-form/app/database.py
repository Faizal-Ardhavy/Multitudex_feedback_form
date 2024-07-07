from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://davi:root@localhost/feedback_form_db"

engine = create_async_engine(DATABASE_URL, echo=True)

# Gunakan async session
async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()

# Dependency
async def get_db():
    async with async_session() as session:
        yield session
