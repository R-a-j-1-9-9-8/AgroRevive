import pickle
import pandas as pd

# Load the model
with open('model/carbon_credit_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_carbon_credits(soil_type, crop_types, regenerative_practice,climate_region,soil_carbon_initial):
    # Create a DataFrame for the new data
    data = pd.DataFrame({
        'Soil_Type':[soil_type],
        'Crop_Type': [crop_types],
        'Regenerative_Practice': [regenerative_practice],
        'Climate_Region' : [climate_region],
        'Soil_Carbon_Initial':[soil_carbon_initial]
    })
    
    # Predict carbon credits
    prediction = model.predict(data)
    return prediction[0]
