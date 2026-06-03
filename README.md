# Retail Shelf Intelligence Pipeline 🛒

An end-to-end batch data engineering pipeline for FMCG retail shelf intelligence built using Apache Kafka, Databricks, Delta Lake, Apache Airflow and databricks dashboards.

---

## 📌 Problem Statement

FMCG companies lose millions in revenue due to out of stock situations at the retail level. This pipeline ingests daily sales, weather and holiday data to identify which stores and product categories are at highest risk of stockouts enabling proactive inventory management.

---

## 🏗️ Architecture
Python Scripts (Data Ingestion)
↓
Apache Kafka (3 Topics: fmcg-sales, weather data, holidays data)
↓
Databricks — Delta Lake Medallion Architecture
├── Bronze Layer (Raw Data)
├── Silver Layer (Cleaned + Joined)
└── Gold Layer (Business KPIs)
↓
Apache Airflow (Daily Orchestration)
↓
Databricks Dashboard (Visualization)
---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Ingestion | Apache Kafka, Python |
| Storage | Databricks Delta Lake |
| Processing | Apache Spark, PySpark |
| Orchestration | Apache Airflow |
| Containerization | Docker |
| Visualization | Databricks Dashboard |
| Version Control | Git, GitHub |

---

## 📦 Data Sources

| Source | Description | Records |
|---|---|---|
| Kaggle FMCG Dataset | Indian retail sales across 8 cities | 100,000 rows |
| Open-Meteo API | Historical weather data for 8 Indian cities | 2,928 rows |
| Python Holidays Library | Indian public holidays 2024 | 16 records |

---

## 🥉🥈🥇 Medallion Architecture

### Bronze Layer
Raw data ingested as-is from all 3 sources into Delta tables:
- `bronze_fmcg_sales` — 100,000 rows
- `bronze_weather` — 2,928 rows
- `bronze_holidays` — 16 rows

### Silver Layer
- Removed duplicates and nulls
- Standardized date formats
- Joined all 3 sources on date and city
- Added `Stock_Risk_Flag` and `is_holiday` columns

### Gold Layer
- `gold_stock_risk` — Stock risk % by city and category
- `gold_weather_sales` — Sales correlation with weather
- `gold_holiday_impact` — Revenue impact of holidays
- `gold_brand_performance` — Brand level KPIs

---

## 📊 Dashboard Screenshots

### Stock Risk Analysis
![Stock Risk](dashboards/stock_risk_analysis.png)

### Weather & Brand Performance
![Weather Brand](dashboards/weather_brand_performance.png)

### Holiday Impact
![Holiday Impact](dashboards/holiday_impact.png)

---

## 🔄 Airflow DAG

The pipeline runs daily at midnight via Apache Airflow:
ingest_data_to_kafka → run_bronze_layer → run_silver_layer → run_gold_layer → notify_completion

---

## 🚀 How to Run

### Prerequisites
- Python 3.10+
- Docker Desktop
- Databricks Community Edition account

### 1. Clone the repo
```bash
git clone https://github.com/EmanMalikk/retail-shelf-intelligence.git
cd retail-shelf-intelligence
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Kafka
```bash
docker-compose -f kafka/docker-compose.yml up -d
```

### 4. Run data ingestion
```bash
python scripts/ingest_to_kafka.py
python scripts/generate_holidays.py
```

### 5. Start Airflow
```bash
docker-compose -f airflow/docker-compose.yml up airflow-init
docker-compose -f airflow/docker-compose.yml up -d
```

---

## 📁 Project Structure
retail-shelf-intelligence/
├── kafka/                    → Kafka Docker setup
├── airflow/                  → Airflow Docker setup
├── dags/                     → Airflow DAG
├── scripts/                  → Python ingestion scripts
├── data/raw/                 → Raw datasets (not pushed to GitHub)
├── notebooks/                → Databricks notebooks
├── dashboards/               → Dashboard screenshots
├── configs/                  → Pipeline configuration
└── requirements.txt          → Python dependencies

---

## 👩‍💻 Author
**Eman Malik**
GitHub: [@EmanMalikk](https://github.com/EmanMalikk)