# 🌦 Weather Data Pipeline with Python & PostgreSQL

## 📌 Project Overview

This project is an end-to-end Data Engineering pipeline that extracts real-time weather data from an external API, stores raw JSON data in PostgreSQL, transforms it into structured format, and loads it into a clean analytics-ready table.

The project follows a layered architecture similar to real-world data engineering systems.

---

## 🏗 Architecture

API → Extract Layer → Raw Table (JSONB) → Transform Layer → Clean Table (Structured) → PostgreSQL

### Layers Implemented:

- Extract Layer
- Raw Load Layer
- Transform Layer
- Clean Load Layer
- Logging & Error Handling

---

## 🛠 Tech Stack

- Python 3.12
- PostgreSQL
- psycopg2
- requests
- python-dotenv
- Logging module
- Git & GitHub

---

## 🗂 Project Structure

weather-data-pipeline/
│
├── config/
│ └── config.py
│
├── extract/
│ └── fetch_weather.py
│
├── transform/
│ └── clean_weather.py
│
├── load/
│ └── load_to_postgres.py
│
├── sql/
│ └── create_table.sql
│
├── main.py
├── requirements.txt
└── .env

## 🔄 Pipeline Flow

1. Extract weather data from API
2. Store raw JSON response into `raw_weather` table
3. Transform JSON into structured fields
4. Load structured data into `clean_weather` table
5. Log success or failure at each step

---

## 🗄 Database Design

### raw_weather
- id
- raw_data (JSONB)
- inserted_at

### clean_weather
- city
- temperature
- humidity
- pressure
- weather_description
- recorded_at
---

## ⚙️ How to Run

### 1️⃣ Install dependencies

pip install -r requirements.txt


### 2️⃣ Setup PostgreSQL
Create database:

CREATE DATABASE weather_db;


Run:

\i sql/create_table.sql


### 3️⃣ Configure Environment
Create `.env` file:


DB_NAME=weather_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
WEATHER_API_KEY=your_api_key

### 4️⃣ Run Pipeline

python main.py


---

## 📊 Engineering Concepts Demonstrated

- ETL Pipeline Design
- Layered Architecture
- Raw vs Clean Data Modeling
- JSONB Storage in PostgreSQL
- Error Handling & Logging
- Database Privilege Management
- Git Version Control
- Conflict Resolution & Rebase

---

## 🚀 Future Improvements

- Add support for multiple cities
- Add Airflow orchestration
- Containerize using Docker
- Deploy to AWS RDS
- Add monitoring & alerting
- Add unit tests

---

## 👤 Author

Jaya Krishnan B
