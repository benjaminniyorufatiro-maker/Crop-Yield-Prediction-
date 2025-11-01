import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open('25RP18751.sav', 'rb'))

# App title
st.title("🌾 Crop Yield Prediction App")
st.write("Designed by **NIYORUFATIRO Benjamin**")
st.write("Enter your crop and environmental details below:")
# --- User Inputs ---
Region = st.selectbox("Select Region", ["North", "South", "East", "West"])
Soil_Type = st.number_input("Soil Type (encoded)", min_value=0, max_value=10, step=1)
Crop = st.number_input("Crop (encoded)", min_value=0, max_value=10, step=1)
Rainfall_mm = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)
Temperature_Celsius = st.number_input("Temperature (°C)", min_value=-10.0, step=0.1)
Fertilizer_Used = st.selectbox("Fertilizer Used", ["TRUE", "FALSE"])
Irrigation_Used = st.selectbox("Irrigation Used", ["TRUE", "FALSE"])
Weather_Condition = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])
Days_to_Harvest = st.number_input("Days to Harvest", min_value=0, step=1)

# --- Encode categorical inputs manually ---
region_map = {"North": 0, "South": 1, "East": 2, "West": 3}
weather_map = {"Sunny": 0, "Rainy": 1, "Cloudy": 2}

encoded_data = {
    'Region': region_map[Region],
    'Soil_Type': Soil_Type,
    'Crop': Crop,
    'Rainfall_mm': Rainfall_mm,
    'Temperature_Celsius': Temperature_Celsius,
    'Fertilizer_Used': 1 if Fertilizer_Used == "TRUE" else 0,
    'Irrigation_Used': 1 if Irrigation_Used == "TRUE" else 0,
    'Weather_Condition': weather_map[Weather_Condition],
    'Days_to_Harvest': Days_to_Harvest
}

# Convert to DataFrame
input_data = pd.DataFrame([encoded_data])

# --- Prediction ---
if st.button("Predict Crop Yield"):
    prediction = model.predict(input_data)
    st.success(f"🌾 Predicted Yield in Tons per Hectal is: **{prediction[0]:.2f}**")