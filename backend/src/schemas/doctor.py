from pydantic import BaseModel, Field

from enum import Enum

class Specialty(str, Enum):
    therapist = "therapist"
    cardiologist = "cardiologist"
    dentist = "dentist"

class DoctorCreate(BaseModel):
    name: str = Field(min_length=2, max_length=30, description="Имя врача")
    specialty: Specialty = Field(description="Специальность врача")
    bio: str = Field(min_length=10, max_length=300, description="Краткое описание врача")

class DoctorRead(BaseModel):
    id: int
    name: str
    specialty: Specialty
    bio: str

    class Config:
        from_attributes = True