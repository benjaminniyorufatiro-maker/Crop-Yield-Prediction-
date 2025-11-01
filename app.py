import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('25RP18751.sav', 'rb'))

st.title("🌾 Crop Yield Prediction App")
st.write("Designed by **NIYORUFATIRO Benjamin**")
st.write("Enter your crop and environmental details below:")

# Dropdowns (automatic selection)
Region = st.selectbox("Select Region", ["North", "South", "East", "West"])
Soil_Type = st.selectbox("Select Soil Type", ["Sandy", "Clay", "Loam", "Silt", "Peaty", "Chalky"])
Crop = st.selectbox("Select Crop", ["Cotton", "Rice", "Barley", "Soybean", "Wheat", "Maize"])
Rainfall_mm = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)
Temperature_Celsius = st.number_input("Temperature (°C)", min_value=-10.0, step=0.1)
Fertilizer_Used = st.selectbox("Fertilizer Used", ["TRUE", "FALSE"])
Irrigation_Used = st.selectbox("Irrigation Used", ["TRUE", "FALSE"])
Weather_Condition = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])
Days_to_Harvest = st.number_input("Days to Harvest", min_value=0, step=1)

# Encode categorical selections for prediction
data = pd.DataFrame([{
    "Region": Region,
    "Soil_Type": Soil_Type,
    "Crop": Crop,
    "Rainfall_mm": Rainfall_mm,
    "Temperature_Celsius": Temperature_Celsius,
    "Fertilizer_Used": 1 if Fertilizer_Used == "TRUE" else 0,
    "Irrigation_Used": 1 if Irrigation_Used == "TRUE" else 0,
    "Weather_Condition": Weather_Condition,
    "Days_to_Harvest": Days_to_Harvest
}])

# Convert categorical features to numbers
data_encoded = pd.get_dummies(data)

# Predict
if st.button("Predict Crop Yield"):
    prediction = model.predict(data_encoded)
    st.success(f"🌾 Predicted Yield: **{prediction[0]:.2f} tons/ha**")
