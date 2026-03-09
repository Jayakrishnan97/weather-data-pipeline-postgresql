import logging
import os

from extract.fetch_weather import fetch_weather_data
from transform.clean_weather import transform_weather_data
from load.load_to_postgres import (
        load_raw_weather,
        load_clean_weather 
)

#ensure logs folder exists
os.makedirs("log", exist_ok = True)

#logging configuration
logging.basicConfig(
        filename = "logs/pipeline.log",
        level=logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    logging.info("Weather pipeline started")

    try:
        #step1:Extract
        raw_data = fetch_weather_data()
        logging.info("Extraction successful")

        #step2: load raw
        load_raw_weather(raw_data)
        logging.info("raw data loaded successfully")

        #step3: transform
        clean_data = transform_weather_data(raw_data)
        logging.info("Transformation successsful")

        #step4: load clean
        load_clean_weather(clean_data)
        logging.info("clean data loaded successfully")

        logging.info("weather pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}", exc_info=True)
        print("pipeline failed. check logs")
    
    else:
        print("pipeline executed succesfully")

if __name__ == "__main__":
    run_pipeline()





