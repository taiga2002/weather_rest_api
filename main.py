from fastapi import FastAPI, Depends, HTTPException
from models import Base
import crud as crud, rest_api.schemas as schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from uuid import UUID

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db=db, location=location)

@app.get("/locations/{location_id}", response_model=schemas.Location)
def get_location(location_id: UUID, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location

@app.get("/locations/", response_model=list[schemas.Location])
def get_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations

@app.get("/location/uuid/", response_model=UUID)
def get_location_id_by_address(location_address: str, db: Session = Depends(get_db)):
    location_id = crud.get_location_uuid_by_address(db=db, location_address=location_address)
    if location_id is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return location_id

@app.put("/locations/{location_id}", response_model=schemas.Location)
def update_location(location_id: UUID, location: schemas.LocationCreate, db: Session = Depends(get_db)):
    updated_location = crud.update_location(db, location_id, location)
    if updated_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return updated_location

@app.delete("/locations/{location_id}", response_model=schemas.Location)
def delete_location(location_id: UUID, db: Session = Depends(get_db)):
    deleted_location = crud.delete_location(db, location_id)
    if deleted_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return deleted_location

@app.post("/lsmweather/", response_model=schemas.LSMWeatherData)
def create_weather(weather_data: schemas.LSMWeatherData, db: Session = Depends(get_db)):
    return crud.create_lsm_weather_data(db=db, weather_data=weather_data)

@app.get("/lsmweather/{weather_id}", response_model=schemas.LSMWeatherData)
def get_lsm_weather(weather_id: UUID, db: Session = Depends(get_db)):
    db_weather_data = crud.get_lsm_weather_data(db=db, weather_id=weather_id)
    if db_weather_data is None:
        raise HTTPException(status_code=404, detail="Weather data not found")
    return db_weather_data

@app.get("/lsmweather/", response_model=list[schemas.LSMWeatherData])
def get_lsm_weather_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lsm_data_list = crud.get_lsm_weather_data_list(db, skip=skip, limit=limit)
    return lsm_data_list

@app.delete("/lsmweather/{weather_id}", response_model=schemas.LSMWeatherData)
def delete_weather(weather_id: UUID, db: Session = Depends(get_db)):
    if not crud.delete_lsm_weather_data(db=db, weather_id=weather_id):
        raise HTTPException(status_code=404, detail="Weather data not found")
    return {"detail": "Weather data deleted"}

@app.put("/lsmweather/{weather_id}", response_model=schemas.LSMWeatherData)
def update_weather(weather_id: UUID, weather_data: schemas.LSMWeatherData, db: Session = Depends(get_db)):
    updated_weather_data = crud.update_lsm_weather_data(db=db, weather_id=weather_id, weather_data=weather_data)
    if updated_weather_data is None:
        raise HTTPException(status_code=404, detail="Weather data not found")
    return updated_weather_data

@app.get("/lsmweather/location/{location_id}", response_model=list[schemas.LSMWeatherData])
def read_weather_by_location(location_id: UUID, db: Session = Depends(get_db)):
    weather_data = crud.get_lsm_weather_data_by_location_id(db=db, location_id=location_id)
    return weather_data

# LSM, GSM, MSM 2024.3.1-> intial time, query how long (hrs)... 30 minutes per data,
# db join and also application join -> unit test/ integration test
# How much db would do??
