from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.doctor import DoctorCreate, DoctorRead
from src.cruds.doctor import create_doctor, get_doctors
from src.database import get_db

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=DoctorRead)
async def add_doctor(data: DoctorCreate, db: AsyncSession = Depends(get_db)):
    return await create_doctor(data, db)

@router.get("/", response_model=list[DoctorRead])
async def list_doctors(db: AsyncSession = Depends(get_db)):
    return await get_doctors(db)