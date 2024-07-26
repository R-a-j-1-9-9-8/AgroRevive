import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Load data
data = pd.read_csv('data/Carbon_Credits.csv')

# Preprocessing
X = data[['Soil_Type', 'Crop_Type', 'Regenerative_Practice','Climate_Region','Soil_Carbon_Initial']]
y = data['Carbon_Credits']

# One-hot encode categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['Soil_Type', 'Crop_Type', 'Regenerative_Practice','Climate_Region'])
    ],
    remainder='passthrough'
)

# Create a pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
with open('model/carbon_credit_predictor.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

print("Model trained and saved successfully!")
