import requests
import logging

from config.config import (
    WEATHER_API_KEY,
    BASE_WEATHER_URL,
    CITY,
    COUNTRY_CODE,
    REQ_TIMEOUT
)

def fetch_weather_data():
    """
    fetch current weather data from openweathermap api returns
    raw json response
    """
    params = {
        "q": f"{CITY},{COUNTRY_CODE}",
        "appid":WEATHER_API_KEY
    }

    try:
        response = requests.get(
            BASE_WEATHER_URL,
            params=params,
            timeout=REQ_TIMEOUT
        )

        if response.status_code != 200:
            logging.error(
                f"Weather API failed | "
                f"Status : {response.status_code} | "
                f"Response: {response.text}"
            )
            response.raise_for_status()

        logging.info("Weather api call successful")
        return response.json()
    
    except requests.exceptions.Timeout:
        logging.error("Weather api request timed out")
        raise

    except requests.exceptions.RequestException as e:
        logging.error(f"Weather api request failed: {e}")
        raise