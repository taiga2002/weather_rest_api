import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database, drop_database
from database import Base
import models, schemas
from crud import (
    create_location,
    get_location,
    get_locations,
    update_location,
    delete_location,
    get_lsm_weather_data,
    get_lsm_weather_data_list,
    create_lsm_weather_data,
    delete_lsm_weather_data,
    update_lsm_weather_data,
    get_lsm_weather_data_by_location_id,
    get_location_uuid_by_address,
)

class TestRestAPI(unittest.TestCase):
    def setUp(self):
        # Set up an in-memory SQLite database for testing
        self.engine = create_engine("sqlite:///:memory:")
        Session = sessionmaker(bind=self.engine)
        self.db = Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        # Tear down the database after each test
        Base.metadata.drop_all(self.engine)
        self.db.close()

    def test_location_crud(self):
        # Create a location
        location_data = schemas.LocationCreate(
            location_address="Test Location",
            latitude=40.0,
            longitude=-75.0
        )
        created_location = create_location(self.db, location_data)
        self.assertIsNotNone(created_location.id)

        # Retrieve the created location
        retrieved_location = get_location(self.db, created_location.id)
        self.assertIsNotNone(retrieved_location)
        self.assertEqual(retrieved_location.location_address, "Test Location")

        # Update the location
        updated_location_data = schemas.LocationCreate(
            location_address="Updated Location",
            latitude=41.0,
            longitude=-76.0
        )
        updated_location = update_location(self.db, created_location.id, updated_location_data)
        self.assertIsNotNone(updated_location)
        self.assertEqual(updated_location.location_address, "Updated Location")
        self.assertEqual(updated_location.latitude, 41.0)
        self.assertEqual(updated_location.longitude, -76.0)

        # Delete the location
        deleted_location = delete_location(self.db, created_location.id)
        self.assertIsNotNone(deleted_location)
        self.assertEqual(deleted_location.id, created_location.id)

class TestWeatherData(unittest.TestCase):
    def setUp(self):
        # Set up an in-memory SQLite database for testing
        self.engine = create_engine("sqlite:///:memory:")
        Session = sessionmaker(bind=self.engine)
        self.db = Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        # Tear down the database after each test
        Base.metadata.drop_all(self.engine)
        self.db.close()

    # def test_lsm_weather_data_crud(self):
    #     # Create LSMWeatherData
    #     weather_data = schemas.LSMWeatherData(
    #         latitude=40.0,
    #         longitude=-75.0,
    #         datetime="2024-03-27 12:00:00",
    #         precipitation=0.5,
    #         temperature=25.0,
    #         humidity=50,
    #         radiation=100,
    #         pressure=1013.25,
    #         jma_radiation=80,
    #         wind_u=5.0,
    #         wind_v=10.0
    #     )
    #     created_weather_data = create_lsm_weather_data(self.db, weather_data)
    #     self.assertIsNotNone(created_weather_data.id)

    #     # Retrieve LSMWeatherData
    #     retrieved_weather_data = get_lsm_weather_data(self.db, created_weather_data.id)
    #     self.assertIsNotNone(retrieved_weather_data)
    #     self.assertEqual(retrieved_weather_data.latitude, 40.0)
    #     self.assertEqual(retrieved_weather_data.longitude, -75.0)
    #     self.assertEqual(retrieved_weather_data.datetime, "2024-03-27 12:00:00")
    #     self.assertEqual(retrieved_weather_data.precipitation, 0.5)
    #     self.assertEqual(retrieved_weather_data.temperature, 25.0)
    #     self.assertEqual(retrieved_weather_data.humidity, 50)
    #     self.assertEqual(retrieved_weather_data.radiation, 100)
    #     self.assertEqual(retrieved_weather_data.pressure, 1013.25)
    #     self.assertEqual(retrieved_weather_data.jma_radiation, 80)
    #     self.assertEqual(retrieved_weather_data.wind_u, 5.0)
    #     self.assertEqual(retrieved_weather_data.wind_v, 10.0)

    #     # Update LSMWeatherData
    #     updated_weather_data = schemas.LSMWeatherData(
    #         latitude=41.0,
    #         longitude=-76.0,
    #         datetime="2024-03-27 13:00:00",
    #         precipitation=0.3,
    #         temperature=24.0,
    #         humidity=55,
    #         radiation=90,
    #         pressure=1012.5,
    #         jma_radiation=70,
    #         wind_u=4.0,
    #         wind_v=9.0
    #     )

    #     updated_weather_data = update_lsm_weather_data(self.db, created_weather_data.id, updated_weather_data)
    #     self.assertIsNotNone(updated_weather_data)
    #     self.assertEqual(updated_weather_data.latitude, 41.0)
    #     self.assertEqual(updated_weather_data.longitude, -76.0)
    #     self.assertEqual(updated_weather_data.datetime, "2024-03-27 13:00:00")
    #     self.assertEqual(updated_weather_data.precipitation, 0.3)
    #     self.assertEqual(updated_weather_data.temperature, 24.0)
    #     self.assertEqual(updated_weather_data.humidity, 55)
    #     self.assertEqual(updated_weather_data.radiation, 90)
    #     self.assertEqual(updated_weather_data.pressure, 1012.5)
    #     self.assertEqual(updated_weather_data.jma_radiation, 70)
    #     self.assertEqual(updated_weather_data.wind_u, 4.0)
    #     self.assertEqual(updated_weather_data.wind_v, 9.0)

    #     # Delete LSMWeatherData
    #     deleted_weather_data = delete_lsm_weather_data(self.db, created_weather_data.id)
    #     self.assertTrue(deleted_weather_data)

if __name__ == "__main__":
    unittest.main()
