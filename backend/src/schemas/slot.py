from pydantic import BaseModel, Field
from datetime import datetime

from src.schemas.doctor import DoctorRead


class SlotCreate(BaseModel):
    doctor_id: int
    start_time: datetime
    end_time: datetime

class SlotRead(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime
    is_booked: bool
    doctor: DoctorRead  # 👈 добавляем объект врача

    class Config:
        from_attributes = True

