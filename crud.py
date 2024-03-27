from sqlalchemy.orm import Session
import rest_api.models as models, rest_api.schemas as schemas
from uuid import UUID

# ------------------
# Location Helper Functions

def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_location(db: Session, location_id: UUID):
    return db.query(models.Location).filter(models.Location.id == location_id).first()

def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

def update_location(db: Session, location_id: UUID, location: schemas.LocationCreate):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if db_location:
        for var, value in vars(location).items():
            setattr(db_location, var, value) if value else None
        db.commit()
        db.refresh(db_location)
    return db_location

def delete_location(db: Session, location_id: UUID):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if db_location:
        db.delete(db_location)
        db.commit()
        return db_location
# ------------------
# LSM Weather Data Helper Functions
def get_lsm_weather_data(db: Session, weather_id: UUID):
    return db.query(models.LSMWeatherData).filter(models.LSMWeatherData.id == weather_id).first()

def get_lsm_weather_data_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LSMWeatherData).offset(skip).limit(limit).all()

def create_lsm_weather_data(db: Session, weather_data: schemas.LSMWeatherData):
    db_weather_data = models.LSMWeatherData(**weather_data.dict())
    db.add(db_weather_data)
    db.commit()
    db.refresh(db_weather_data)
    return db_weather_data

def delete_lsm_weather_data(db: Session, weather_id: UUID):
    db_weather_data = db.query(models.LSMWeatherData).filter(models.LSMWeatherData.id == weather_id).first()
    if db_weather_data:
        db.delete(db_weather_data)
        db.commit()
        return True
    return False

def update_lsm_weather_data(db: Session, weather_id: UUID, weather_data: schemas.LSMWeatherData):
    db_weather_data = db.query(models.LSMWeatherData).filter(models.LSMWeatherData.id == weather_id).first()
    if db_weather_data:
        for key, value in weather_data.dict().items():
            setattr(db_weather_data, key, value)
        db.commit()
        db.refresh(db_weather_data)
        return db_weather_data
    return None

def get_lsm_weather_data_by_location_id(db: Session, location_id: UUID):
    return db.query(models.LSMWeatherData).join(models.LSMLocation, models.LSMWeatherData.id == models.LSMLocation.lsm_weather_id).filter(models.LSMLocation.location_id == location_id).all()

def get_location_uuid_by_address(db: Session, location_address: str):
    location = db.query(models.Location).filter(models.Location.location_address == location_address).first()
    return location.id if location else None