--raw weather storage(json)

CREATE TABLE IF NOT EXISTS raw_weather(
    id SERIAL PRIMARY KEY,
    raw_response JSONB NOT NULL,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


--cleaned weather data

CREATE TABLE IF NOT EXISTS clean_weather(
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    date DATE NOT NULL,
    temperature FLOAT,
    feels_like FLOAT,
    humidity INT,
    pressure INT,
    weather_main TEXT,
    weather_description TEXT,
    wind_speed FLOAT,
    fetched_at TIMESTAMP,
    UNIQUE (city, date)
);
