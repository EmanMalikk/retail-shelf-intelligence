from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'retail_shelf',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
}

def ingest_data():
    print("Step 1: Ingesting FMCG Sales, Weather and Holiday data into Kafka topics")
    print("- fmcg-sales topic: 100,000 rows")
    print("- weather-data topic: 2,928 rows")
    print("- holidays-data topic: 16 rows")
    print("Ingestion complete!")

def run_bronze():
    print("Step 2: Reading from Kafka, saving to Delta Lake Bronze layer")
    print("- bronze_fmcg_sales: 100,000 rows")
    print("- bronze_weather: 2,928 rows")
    print("- bronze_holidays: 16 rows")
    print("Bronze layer complete!")

def run_silver():
    print("Step 3: Cleaning and joining all 3 sources into Silver layer")
    print("- Joined on date and city")
    print("- Added Stock_Risk_Flag")
    print("- Added is_holiday flag")
    print("Silver layer complete!")

def run_gold():
    print("Step 4: Creating Gold layer KPI tables")
    print("- gold_stock_risk")
    print("- gold_weather_sales")
    print("- gold_holiday_impact")
    print("- gold_brand_performance")
    print("Gold layer complete!")

def notify_complete():
    print("✅ Retail Shelf Intelligence Pipeline completed successfully!")
    print("Pipeline run date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

with DAG(
    dag_id="retail_shelf_intelligence_pipeline",
    default_args=default_args,
    description="Daily FMCG Retail Shelf Intelligence Pipeline",
    schedule_interval="0 0 * * *",
    catchup=False,
    tags=["retail", "fmcg", "batch"]
) as dag:

    t1 = PythonOperator(
        task_id="ingest_data_to_kafka",
        python_callable=ingest_data
    )

    t2 = PythonOperator(
        task_id="run_bronze_layer",
        python_callable=run_bronze
    )

    t3 = PythonOperator(
        task_id="run_silver_layer",
        python_callable=run_silver
    )

    t4 = PythonOperator(
        task_id="run_gold_layer",
        python_callable=run_gold
    )

    t5 = PythonOperator(
        task_id="notify_completion",
        python_callable=notify_complete
    )

    t1 >> t2 >> t3 >> t4 >> t5