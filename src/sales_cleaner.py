# src/sales_cleaner.py

"""
Clean and standardize raw sales data.
Handles missing values, invalid entries, and date normalization.
Outputs cleaned CSV to data/processed/
"""

import pandas as pd
import os

# 🔄 Load raw data
raw_path = "data/raw/sales_data.csv"
df = pd.read_csv(raw_path)

# 🧹 Drop rows with missing critical fields
df.dropna(subset=["date", "region", "pattern_name", "units_sold", "price_per_unit"], inplace=True)

# 🧪 Fix date format and remove invalid dates
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=["date"])

# 🧼 Standardize text columns
df['region'] = df['region'].str.title().str.strip()
df['pattern_name'] = df['pattern_name'].str.replace("_", " ").str.title().str.strip()

# ➕ Calculate revenue
df['revenue'] = df['units_sold'] * df['price_per_unit']

# 📦 Save cleaned version
output_path = "data/processed/cleaned_sales_data.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"✅ Cleaned sales data saved to {output_path}")
