from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.models.appointment_slots import AppointmentSlot
from src.schemas.slot import SlotCreate

async def create_slot(db: AsyncSession, data: SlotCreate):
    slot = AppointmentSlot(**data.model_dump())
    db.add(slot)
    await db.commit()
    await db.refresh(slot)
    return slot

async def get_slots_by_doctor(db: AsyncSession, doctor_id: int):
    """Получить все слоты конкретного доктора с подгруженным doctor"""
    result = await db.execute(
        select(AppointmentSlot)
        .options(selectinload(AppointmentSlot.doctor))
        .where(AppointmentSlot.doctor_id == doctor_id)
    )
    return result.scalars().all()

async def book_slot(db: AsyncSession, slot_id: int):
    # Получаем слот с уже загруженным doctor
    result = await db.execute(
        select(AppointmentSlot)
        .options(selectinload(AppointmentSlot.doctor))
        .where(AppointmentSlot.id == slot_id)
    )
    slot = result.scalar_one_or_none()

    if not slot:
        return None

    slot.is_booked = True
    await db.commit()
    await db.refresh(slot)

    # Теперь слот возвращается с уже подгруженным doctor
    return slot

async def get_all_slots(db: AsyncSession):
    """Получить все слоты с подгруженными докторами"""
    result = await db.execute(
        select(AppointmentSlot).options(selectinload(AppointmentSlot.doctor))
    )
    return result.scalars().all()
