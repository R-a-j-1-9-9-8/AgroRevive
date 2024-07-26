import streamlit as st
import pandas as pd
from plan_predictor import predict_regenerative_practices


st.title("Regenerative Farming Planner")
    
    # Form to input carbon credit details
st.subheader("Enter Farm Details for suggesting Regenerative Farming")
    
form = st.form(key="regenerative_farming_form")
    #farm_name = form.text_input("Farm Name")
soil_type = form.selectbox("Soil Types", ['Clay', 'Silt', 'Sand', 'Loam'])
farm_size = form.number_input("Farm Size (acres)", min_value=0.0)
crop_selection = form.selectbox("Crop Selection", ['Corn', 'Soybeans', 'Wheat', 'Cover_Crops'])
water_availability = form.selectbox("Water Availability", ['High', 'Medium', 'Low'])
climate = form.selectbox("Climate", ['Temperate', 'Tropical', 'Arid', 'Semi-Arid'])
topography = form.selectbox("Topography", ['Flat', 'Sloping', 'Hilly', 'Mountainous'])
livestock_grazing = form.selectbox("Livestock Grazing", ['Rotational', 'Continuous', 'No_Grazing'])
    
predict_button = form.form_submit_button(label="Suggest Regenerative Practise")

input_data = pd.DataFrame({
    'Soil_Type': [soil_type],
    'Climate': [climate],
    'Topography': [topography],
    'Water_Availability': [water_availability],
    'Crop_Selection': [crop_selection],
    'Livestock_Grazing': [livestock_grazing],
    'Farm_Size': [farm_size]
})
    
if predict_button:
        plan_prediction = predict_regenerative_practices(input_data)
        plan_prediction = plan_prediction[0].replace("_"," ") 
        st.success(f"Suggested Regenerative Practise : {plan_prediction}")
        