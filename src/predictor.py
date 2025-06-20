# src/predict.py

import pandas as pd
import joblib
from datetime import datetime

# 📁 Load the trained model
model = joblib.load('models/rf_units_predictor.pkl')

# 📄 Example new data to predict
future_data = pd.DataFrame({
    'date': pd.date_range("2024-07-01", periods=5),
    'pattern_name': ['Metis_Sash', 'Navajo_Weave', 'Haida_Formline', 'Cree_Beadwork', 'Inuit_Tapestry']
})

# 🧪 Feature engineering (match train script)
future_data['day'] = future_data['date'].dt.day
future_data['month'] = future_data['date'].dt.month
future_data['weekday'] = future_data['date'].dt.weekday
future_data['pattern_encoded'] = future_data['pattern_name'].astype('category').cat.codes

# 🔍 Predict
X_future = future_data[['day', 'month', 'weekday', 'pattern_encoded']]
future_data['predicted_units'] = model.predict(X_future)

# 💾 Save results
future_data[['date', 'pattern_name', 'predicted_units']].to_csv('outputs/predictions.csv', index=False)
print("✅ Predictions saved to outputs/predictions.csv")
