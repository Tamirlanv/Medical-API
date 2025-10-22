from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.config.settings import settings

# Создание движка
engine = create_async_engine(settings.DATABASE_URL, echo=False)

# Сессия
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для моделей
Base = declarative_base()

# Зависимость для FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session