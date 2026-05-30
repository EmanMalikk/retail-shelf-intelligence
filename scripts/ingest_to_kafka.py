import requests
import pandas as pd
from datetime import datetime

# Indian cities with coordinates (matching our FMCG dataset)
CITIES = {
    "Mumbai":    {"lat": 19.0760, "lon": 72.8777},
    "Delhi":     {"lat": 28.6139, "lon": 77.2090},
    "Bangalore": {"lat": 12.9716, "lon": 77.5946},
    "Chennai":   {"lat": 13.0827, "lon": 80.2707},
    "Kolkata":   {"lat": 22.5726, "lon": 88.3639},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "Pune":      {"lat": 18.5204, "lon": 73.8567},
    "Ahmedabad": {"lat": 23.0225, "lon": 72.5714},
}

def fetch_weather(city, lat, lon, start_date="2024-01-01", end_date="2024-12-31"):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Asia/Kolkata"
    }
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data["daily"])
    df["city"] = city
    df.rename(columns={"time": "date"}, inplace=True)
    return df

def fetch_all_cities():
    all_data = []
    for city, coords in CITIES.items():
        print(f"Fetching weather for {city}...")
        df = fetch_weather(city, coords["lat"], coords["lon"])
        all_data.append(df)
    
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv("data/raw/weather_2024.csv", index=False)
    print(f"Done! {len(final_df)} rows saved to data/raw/weather_2024.csv")

if __name__ == "__main__":
    fetch_all_cities()