from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.database import get_db
from src.schemas.patient import PatientCreate, PatientRead
from src.models.patients import Patient
from src.cruds.patient import create_patient

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/", response_model=PatientRead)
async def register_patient(data: PatientCreate, db: AsyncSession = Depends(get_db)):
    """Регистрация нового пациента"""
    return await create_patient(db, data)


@router.get("/", response_model=list[PatientRead])
async def get_patients(db: AsyncSession = Depends(get_db)):
    """Получить список всех пациентов"""
    result = await db.execute(select(Patient))
    return result.scalars().all()
