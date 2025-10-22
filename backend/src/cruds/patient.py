from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from src.models.patients import Patient
from src.schemas.patient import PatientCreate

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


async def create_patient(db: AsyncSession, data: PatientCreate):
    existing = await db.execute(select(Patient).where(Patient.email == data.email))
    if existing.scalar():
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")

    hashed_password = pwd_context.hash(data.password)

    patient = Patient(
        name=data.name,
        email=str(data.email),
        password=hashed_password
    )

    db.add(patient)
    await db.commit()
    await db.refresh(patient)
    return patient

