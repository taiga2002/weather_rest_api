from pydantic import BaseModel
from typing import Optional, List, Union
from uuid import UUID
from datetime import datetime

class LocationCreate(BaseModel):
    location_address: str
    latitude: float
    longitude: float

class Location(LocationCreate):
    id: Optional[UUID] = None

    class Config:
        from_attributes = True

class WeatherDataBase(BaseModel):
    latitude: float
    longitude: float
    datetime: datetime
    precipitation: float
    temperature: float
    humidity: int
    radiation: float
    pressure: float
    jma_radiation: float
    wind_u: float
    wind_v: float

    class Config:
        from_attributes = True

class LSMWeatherData(WeatherDataBase):
    id: UUID

    class Config:
        from_attributes = True

class GSMWeatherData(WeatherDataBase):
    id: UUID

    class Config:
        from_attributes = True

class MSMWeatherData(WeatherDataBase):
    id: UUID

    class Config:
        from_attributes = True

class LSMLocation(BaseModel):
    id: UUID
    location_id: UUID
    lsm_weather_id: UUID

    class Config:
        from_attributes = True

class GSMLocation(BaseModel):
    id: UUID
    location_id: UUID
    gsm_weather_id: UUID

    class Config:
        from_attributes = True

class MSMLocation(BaseModel):
    id: UUID
    location_id: UUID
    msm_weather_id: UUID
    
    class Config:
        from_attributes = True
