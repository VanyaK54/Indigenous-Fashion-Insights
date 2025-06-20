# src/train_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# 📁 Load cleaned data
df = pd.read_csv('data/processed/daily_units_by_pattern.csv')

# 🧪 Feature Engineering
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.weekday
df['pattern_encoded'] = df['pattern_name'].astype('category').cat.codes

# 🎯 Define features and target
X = df[['day', 'month', 'weekday', 'pattern_encoded']]
y = df['daily_units']

# 📚 Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🏗️ Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🧠 Evaluate
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"✅ RMSE: {rmse:.2f}")

# 💾 Save model
joblib.dump(model, 'models/rf_units_predictor.pkl')
print("🎉 Model saved to models/rf_units_predictor.pkl")
