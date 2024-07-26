import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# Load data
data = pd.read_csv('data/plan.csv')

label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Split data into features and target
X = data.drop('Regenerative_Practices', axis=1)
y = data['Regenerative_Practices']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model and label encoders
dump(model, 'model/plan_model.joblib')
dump(label_encoders, 'model/plan_label_encoders.joblib')

print("Model and label encoders saved successfully.")

