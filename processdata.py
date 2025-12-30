import pandas as pd
from pathlib import Path

# Path to the data directory
DATA_DIR = Path("data")

# all daily sales CSV files
csv_files = DATA_DIR.glob("daily_sales_data_*.csv")

processed_frames = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keeps only Pink Morsels
    df = df[df["product"] == "Pink Morsel"]

    # Creates Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Selected required fields
    df = df[["Sales", "date", "region"]]

    processed_frames.append(df)

# Combines all processed data
final_df = pd.concat(processed_frames, ignore_index=True)

# Saves combined output
final_df.to_csv("processed_sales.csv", index=False)

print("✅ Processing complete. File saved as processed_sales.csv")
