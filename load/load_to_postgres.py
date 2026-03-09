import json
import logging
import psycopg2
from psycopg2.extras import Json
from config.config import DB_CONFIG

def get_db_coonection():

    """
    create and return a postgresql connection
    """

    return psycopg2.connect(
        host = DB_CONFIG["host"],
        port = DB_CONFIG["port"],
        dbname = DB_CONFIG["dbname"],
        user = DB_CONFIG["user"],
        password = DB_CONFIG["password"]
    )

def load_raw_weather(raw_data: dict):
    """
    Insert raw weather Json data into weather _raw table
    """
    conn = None
    cursor = None

    try:
        conn = get_db_coonection()
        cursor = conn.cursor()
        
        insert_query = """
            INSERT INTO raw_weather (raw_response)
            values (%s)
            """
        cursor.execute(insert_query, (json.dumps(raw_data),))
        conn.commit()

        logging.info("Raw weather data inserted into raw_weather table")


    except Exception as e:
        if conn:
            conn.rollback()
        logging.error(f"Failed to load raw_weather data: {e}", exc_info=True)
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def load_clean_weather(clean_data: dict):
    """
    Insert cleaned weather data into clean_weather table
    """

    conn = None
    cursor = None

    try:
        conn = get_db_coonection()
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO clean_weather(
            city,
            date,
            temperature,
            feels_like,
            humidity,
            pressure,
            weather_main,
            weather_description,
            wind_speed,
            fetched_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (city, date) DO NOTHING
        """

        cursor.execute(insert_query, (
            clean_data["city"],
            clean_data["date"],
            clean_data["temperature"],
            clean_data["feels_like"],
            clean_data["humidity"],
            clean_data["pressure"],
            clean_data["weather_main"],
            clean_data["weather_description"],
            clean_data["wind_speed"],
            clean_data["fetched_at"]
        ))

        conn.commit()
        logging.info("Clean weather data inserted into clean_weather table")

    
    except Exception as e:
        if conn:
            conn.rollback()
        logging.error(f"Failed to load clean_weather data: {e}", exc_info = True)
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()