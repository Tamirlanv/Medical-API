from src.database import AsyncSessionLocal, engine, Base
from src.config.doctors_seeds import seed_doctors
from src.config.slots_seeds import seed_slots
import logging

logger = logging.getLogger(__name__)

async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ Таблицы созданы")

    logger.info("🚀 Инициализация базы данных...")
    async with AsyncSessionLocal() as session:
        logger.info("🌱 Сидируем докторов...")
        await seed_doctors(session)
        logger.info("✅ Доктора сидированы.")

        logger.info("🕐 Сидируем слоты...")
        await seed_slots(session)
        logger.info("✅ Слоты сидированы.")

