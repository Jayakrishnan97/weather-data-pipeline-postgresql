import os
from dotenv import load_dotenv

load_dotenv()

#api key

WEATHER_API_KEY =  os.getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    raise ValueError("Weather api key not found")

#base api config
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

#default location

CITY = "Hyderabad"
COUNTRY_CODE = "IN" #INDIA

#request settings
REQ_TIMEOUT = 10 #seconds


#postgreSQL config

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port":int(os.getenv("DB_PORT", 5432)),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


#SAFETY CHECK (very important)

missing = [k for k, v in DB_CONFIG.items() if not v]
if missing:
    raise ValueError(f"Missing db config values: {missing}")
