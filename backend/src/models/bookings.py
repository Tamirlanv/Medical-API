from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    slot_id = Column(Integer, ForeignKey("appointment_slots.id"), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    patient = relationship("Patient")
    slot = relationship("AppointmentSlot")
