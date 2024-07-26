import streamlit as st
import pandas as pd
from carbon_predictor import predict_carbon_credits


st.title("Sell Carbon Credits")
    
    # Form to input carbon credit details
st.subheader("Enter Farm Details for Carbon Credit Prediction")
    
form = st.form(key="carbon_credits_form")
    #farm_name = form.text_input("Farm Name")
soil_type = form.selectbox("Soil Types", ['clay', 'silt', 'sand', 'loam'])
farm_size = form.number_input("Farm Size (acres)", min_value=0.0)
crop_types = form.selectbox("Crop Types", ['corn', 'soybeans', 'wheat', 'cover crops'])
regenerative_practice = form.selectbox("Regenerative Practice", ['no-till', 'reduced-till', 'cover crops', 'crop rotation'])
climate_region = form.selectbox("Climate Region", ['temperate', 'tropical', 'arid', 'semi-arid'])
soil_carbon_initial = form.number_input("Soil Carbon Initial (T/Ha)", min_value=0.0)
    
predict_button = form.form_submit_button(label="Predict Carbon Credits")
    
if predict_button:
    credits_prediction = predict_carbon_credits(soil_type, crop_types, regenerative_practice,climate_region,soil_carbon_initial)
    st.success(f"Estimated Carbon Credits: ₹{round(credits_prediction * farm_size,2)}")
        
