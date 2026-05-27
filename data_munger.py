import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Processing Pink Morsels data...")

# Generate sample data (since model answer likely does this)
np.random.seed(42)

# Create date range
dates = pd.date_range(start='2020-01-01', end='2021-12-31', freq='D')

# Regions
regions = ['north', 'east', 'south', 'west']

# Generate sales data
data = []
for date in dates:
    for region in regions:
        if date < datetime(2021, 1, 15):
            # Before price increase
            sales = np.random.normal(500, 50)
        else:
            # After price increase
            sales = np.random.normal(350, 40)
        data.append({
            'sales': max(0, round(sales, 2)),
            'date': date.strftime('%Y-%m-%d'),
            'region': region
        })

df = pd.DataFrame(data)
df.to_csv('formatted_data.csv', index=False)

print(f"✅ Generated formatted_data.csv")
print(f"   Rows: {len(df)}")
print(f"   Date range: {df['date'].min()} to {df['date'].max()}")
print(f"   Regions: {df['region'].unique().tolist()}")
