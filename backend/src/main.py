import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.doctors_seeds import seed_doctors
from src.config.slots_seeds import seed_slots
from src.database import AsyncSessionLocal
from src.routers import doctor, patient, slot, booking
from src.config.startup import on_startup

app = FastAPI(title="Medical API")


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(name)s: %(message)s"
)

# Отключаем SQLAlchemy engine логи
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.on_event("startup")
async def startup():
    # Создаём таблицы и сидируем докторов
    await on_startup()

    # Создаём сессию и сидируем слоты
    async with AsyncSessionLocal() as session:
        await seed_doctors(session)
        await seed_slots(session)

app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(slot.router)
app.include_router(booking.router)


