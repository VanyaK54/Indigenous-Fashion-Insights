# Streamlit app to display predictions and dashboards
import streamlit as st
from src.image_classifier import build_cnn

st.title("🧣 Indigenous Fashion Insight Demo")

st.sidebar.header("Upload Pattern Image")
img_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "png"])

if img_file:
    st.image(img_file, caption="Uploaded Image", use_column_width=True)
    st.success("Run prediction... (logic to be implemented)")

st.sidebar.header("View Dashboards")
st.markdown("👉 Power BI / Tableau dashboards will be embedded here")
