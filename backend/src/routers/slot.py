from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.schemas.slot import SlotCreate, SlotRead
from src.cruds.slot import create_slot, get_slots_by_doctor, book_slot, get_all_slots

router = APIRouter(prefix="/slots", tags=["Slots"])


@router.post("/", response_model=SlotRead)
async def create_slot_route(data: SlotCreate, db: AsyncSession = Depends(get_db)):
    """Создать новый слот для доктора"""
    return await create_slot(db, data)


@router.get("/{doctor_id}", response_model=list[SlotRead])
async def get_doctor_slots(doctor_id: int, db: AsyncSession = Depends(get_db)):
    """Получить все слоты конкретного доктора"""
    return await get_slots_by_doctor(db, doctor_id)


@router.get("/", response_model=list[SlotRead])
async def get_slots_route(db: AsyncSession = Depends(get_db)):
    """Получить все слоты"""
    return await get_all_slots(db)


@router.post("/{slot_id}/book", response_model=SlotRead)
async def book_slot_route(slot_id: int, db: AsyncSession = Depends(get_db)):
    """Забронировать слот"""
    return await book_slot(db, slot_id)
