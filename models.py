from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from rest_api.database import Base
import uuid

class Location(Base):
    __tablename__ = "location"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_address = Column(String(255))
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))

class LSMLocation(Base):
    __tablename__ = "lsm_location"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = Column(UUID(as_uuid=True), ForeignKey('location.id'))
    lsm_weather_id = Column(UUID(as_uuid=True), ForeignKey('lsm_weather_data.id'))


class LSMWeatherData(Base):
    __tablename__ = "lsm_weather_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))
    datetime = Column(DateTime)
    precipitation = Column(DECIMAL(5,2))
    temperature = Column(DECIMAL(3,1))
    humidity = Column(Integer)
    radiation = Column(DECIMAL(5,3))
    pressure = Column(DECIMAL(5,1))
    jma_radiation = Column(DECIMAL(5,3))
    wind_u = Column(DECIMAL(3,1))
    wind_v = Column(DECIMAL(3,1))

class GSMLocation(Base):
    __tablename__ = "gsm_location"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = Column(UUID(as_uuid=True), ForeignKey('location.id'))
    lsm_weather_id = Column(UUID(as_uuid=True), ForeignKey('gsm_weather_data.id'))


class GSMWeatherData(Base):
    __tablename__ = "gsm_weather_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))
    datetime = Column(DateTime)
    precipitation = Column(DECIMAL(5,2))
    temperature = Column(DECIMAL(3,1))
    humidity = Column(Integer)
    radiation = Column(DECIMAL(5,3))
    pressure = Column(DECIMAL(5,1))
    jma_radiation = Column(DECIMAL(5,3))
    wind_u = Column(DECIMAL(3,1))
    wind_v = Column(DECIMAL(3,1))

class MSMLocation(Base):
    __tablename__ = "msm_location"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = Column(UUID(as_uuid=True), ForeignKey('location.id'))
    lsm_weather_id = Column(UUID(as_uuid=True), ForeignKey('msm_weather_data.id'))


class GSMWeatherData(Base):
    __tablename__ = "msm_weather_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))
    datetime = Column(DateTime)
    precipitation = Column(DECIMAL(5,2))
    temperature = Column(DECIMAL(3,1))
    humidity = Column(Integer)
    radiation = Column(DECIMAL(5,3))
    pressure = Column(DECIMAL(5,1))
    jma_radiation = Column(DECIMAL(5,3))
    wind_u = Column(DECIMAL(3,1))
    wind_v = Column(DECIMAL(3,1))


