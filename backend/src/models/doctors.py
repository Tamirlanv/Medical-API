from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    bio = Column(String)

    slots = relationship("AppointmentSlot", back_populates="doctor", cascade="all, delete")