import numpy as np
import pandas as pd
from joblib import load

# Load the model and label encoders
model = load('model/plan_model.joblib')
label_encoders = load('model/plan_label_encoders.joblib')

def predict_regenerative_practices(input_data):
    # Encode input data
    for column in input_data.select_dtypes(include=['object']).columns:
        input_data[column] = label_encoders[column].transform(input_data[column])
    
    # Make predictions
    predictions = model.predict(input_data)
    
    # Decode predictions
    predictions = label_encoders['Regenerative_Practices'].inverse_transform(predictions)
    
    return predictions
