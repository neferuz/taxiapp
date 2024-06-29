from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    verified = Column(Boolean, default=False)
    registered_on = Column(DateTime, default=datetime.datetime.utcnow)

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_available = Column(Boolean, default=True)
    verified = Column(Boolean, default=False)
    location = Column(String)
    rating = Column(Float, default=0.0)
    total_trips = Column(Integer, default=0)

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True, index=True)
    start_location = Column(String)
    end_location = Column(String)
    cost = Column(Float)
    status = Column(String, default="pending")
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    driver = relationship("Driver")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    start_time = Column(DateTime)
    end_time = Column(DateTime)
