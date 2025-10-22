from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.schemas.bookings import BookingCreate, BookingRead
from src.cruds.booking import create_booking

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingRead)
async def book_slot(data: BookingCreate, db: AsyncSession = Depends(get_db)):
    return await create_booking(db, data)
