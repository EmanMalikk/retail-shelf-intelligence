import pandas as pd
import json
from kafka import KafkaProducer

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
)

def send_to_kafka(topic, df):
    print(f"Sending {len(df)} rows to topic: {topic}")
    for _, row in df.iterrows():
        producer.send(topic, value=row.to_dict())
    producer.flush()
    print(f"Done sending to {topic}!")

def ingest_fmcg_sales():
    try:
        df = pd.read_csv("data/raw/Indian FMCG Retail Sales  Customer  Inventory (2024).csv")
        print(f"FMCG file loaded: {df.shape}")
        send_to_kafka("fmcg-sales", df)
    except Exception as e:
        print(f"Error loading FMCG file: {e}")

def ingest_weather():
    df = pd.read_csv("data/raw/weather_2024.csv")
    send_to_kafka("weather-data", df)

def ingest_holidays():
    df = pd.read_csv("data/raw/holidays_2024.csv")
    send_to_kafka("holidays-data", df)

if __name__ == "__main__":
    print("Starting ingestion pipeline...")
    ingest_fmcg_sales()
    ingest_weather()
    ingest_holidays()
    print("All data sent to Kafka successfully!")