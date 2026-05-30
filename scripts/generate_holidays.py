import holidays
import pandas as pd

def generate_indian_holidays():
    india_holidays = holidays.India(years=2024)
    
    records = []
    for date, name in sorted(india_holidays.items()):
        records.append({
            "date": str(date),
            "holiday_name": name,
            "is_holiday": 1
        })
    
    df = pd.DataFrame(records)
    df.to_csv("data/raw/holidays_2024.csv", index=False)
    print(f"Done! {len(df)} holidays saved to data/raw/holidays_2024.csv")

if __name__ == "__main__":
    generate_indian_holidays()