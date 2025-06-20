# app/streamlit_app.py

import streamlit as st
import pandas as pd
import joblib
from datetime import date

# Load model
model = joblib.load('models/rf_units_predictor.pkl')

# Available pattern types
patterns = ['Metis_Sash', 'Navajo_Weave', 'Haida_Formline', 'Cree_Beadwork', 'Inuit_Tapestry']

# Sidebar inputs
st.sidebar.header("🧣 Predict Outfit Demand")
selected_date = st.sidebar.date_input("Select a Date", date(2024, 7, 1))
selected_pattern = st.sidebar.selectbox("Select Pattern", patterns)

# Feature engineering
day = selected_date.day
month = selected_date.month
weekday = selected_date.weekday()
pattern_encoded = patterns.index(selected_pattern)

# Prediction
X_input = pd.DataFrame([[day, month, weekday, pattern_encoded]],
                       columns=['day', 'month', 'weekday', 'pattern_encoded'])
predicted_units = model.predict(X_input)[0]

# Display
st.title("📈 Indigenous Pattern Demand Forecast")
st.write(f"### 📅 Date: {selected_date}")
st.write(f"### 🧵 Pattern: {selected_pattern}")
st.success(f"🔮 Predicted Units Sold: **{predicted_units:.2f}**")

# Optional: Show preview of recent predictions
try:
    df = pd.read_csv("outputs/predictions.csv")
    st.subheader("📊 Recent Predictions")
    st.dataframe(df.tail(5))
except:
    st.info("No recent predictions available yet.")
