from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from src.models.bookings import Booking
from src.models.appointment_slots import AppointmentSlot
from src.schemas.bookings import BookingCreate

async def create_booking(db: AsyncSession, data: BookingCreate):
    slot = await db.get(AppointmentSlot, data.slot_id)
    if not slot:
        raise HTTPException(status_code=404, detail="Слот не найден")
    if slot.is_booked:
        raise HTTPException(status_code=400, detail="Слот уже занят")

    slot.is_booked = True
    booking = Booking(patient_id=data.patient_id, slot_id=data.slot_id)
    db.add(booking)
    await db.commit()
    await db.refresh(booking)
    return booking
