from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    patient_id: int
    slot_id: int

class BookingRead(BaseModel):
    id: int
    patient_id: int
    slot_id: int
    created_at: datetime

    class Config:
        from_attributes = True
