from pydantic import BaseModel, EmailStr, Field

class PatientCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=4, max_length=50)

class PatientRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
