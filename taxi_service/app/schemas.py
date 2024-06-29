from pydantic import BaseModel, Field
from datetime import datetime
class UserBase(BaseModel):
    phone_number: str = Field(..., pattern="^\+?1?\d{9,15}$")

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    verified: bool
    class Config:
        orm_mode = True

class DriverBase(BaseModel):
    phone_number: str = Field(..., pattern="^\+?1?\d{9,15}$")

class DriverCreate(DriverBase):
    password: str

class Driver(DriverBase):
    id: int
    is_available: bool
    location: str
    rating: float
    total_trips: int
    verified: bool
    class Config:
        orm_mode = True

class TripBase(BaseModel):
    start_location: str
    end_location: str

class TripCreate(TripBase):
    pass

class Trip(TripBase):
    id: int
    cost: float
    status: str
    driver_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
    class Config:
        orm_mode = True
