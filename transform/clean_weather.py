from datetime import datetime

def kelvin_to_celsius(kelvin_temp:float) -> float:
    return round(kelvin_temp - 273.15, 2)

def transform_weather_data(raw_data:dict) -> dict:
    """
    transform raw weather json into structered clean data"""

    #extract nested values 

    city = raw_data.get("name")
    timestamp = raw_data.get("dt")

    main_data = raw_data.get("main", {})
    weather_data = raw_data.get("weather", [{}])[0]
    wind_data = raw_data.get("wind", {})

    temperature = kelvin_to_celsius(main_data.get("temp"))
    feels_like = kelvin_to_celsius(main_data.get("feels_like"))
    humidity = main_data.get("humidity")
    pressure = main_data.get("pressure")

    weather_main = weather_data.get("main")
    weather_description = weather_data.get("description")

    wind_speed = wind_data.get("speed")

    #convert timestamp to date

    date_value = datetime.utcfromtimestamp(timestamp).date()
    fetched_at = datetime.utcnow()

    clean_data = {
        "city": city,
        "date":date_value,
        "temperature": temperature,
        "feels_like":feels_like,
        "humidity": humidity,
        "pressure": pressure,
        "weather_main": weather_main,
        "weather_description": weather_description,
        "wind_speed": wind_speed,
        "fetched_at": fetched_at
    }

    return clean_data