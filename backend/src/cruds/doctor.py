from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.doctors import Doctor
from src.schemas.doctor import DoctorCreate

async def create_doctor(data: DoctorCreate, db: AsyncSession) -> Doctor:
    doctor = Doctor(**data.model_dump())
    db.add(doctor)
    await db.commit()
    await db.refresh(doctor)
    return doctor

async def get_doctors(db: AsyncSession):
    result = await db.execute(select(Doctor))
    return result.scalars().all()