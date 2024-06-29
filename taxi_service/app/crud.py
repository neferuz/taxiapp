from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(phone_number=user.phone_number, hashed_password=fake_hashed_password, is_active=True, verified=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_driver(db: Session, driver: schemas.DriverCreate):
    fake_hashed_password = driver.password + "notreallyhashed"
    db_driver = models.Driver(phone_number=driver.phone_number, hashed_password=fake_hashed_password, is_available=True, verified=False)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def create_trip(db: Session, trip: schemas.TripCreate, cost: float, driver_id: int, user_id: int):
    db_trip = models.Trip(start_location=trip.start_location, end_location=trip.end_location, cost=cost, status="pending", driver_id=driver_id, user_id=user_id)
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip
