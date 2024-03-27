# Weather REST API

## Overview
This Weather REST API, developed in Python and FastAPI, serves as a bridge between users and the Japan Meteorological Agency's (気象庁) weather data. Utilizing SQLite for database management, it offers an efficient way to store and retrieve weather information.

## Features
- Fetch and store weather data from the Japan Meteorological Agency.
- Manage weather data using SQLite.
- CRUD operations for weather data.

## Installation
- Clone the repository.
- Install dependencies: `pip install -r requirements.txt`.
- Run `uvicorn main:app --reload`
- If you call `http://127.0.0.1:8000/docs`, you would get documentation on the webpage.
  -> [PDF version] (https://drive.google.com/file/d/1TMpPDxugGDOZV88B8HBW1sz_H5p9VjDF/view?usp=sharing)
## Usage
- Use endpoints to perform CRUD operations on weather data.

## Contributing
Contributions are welcome. Please open an issue or pull request.
