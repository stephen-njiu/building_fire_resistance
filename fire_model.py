# -*- coding: utf-8 -*-
"""fire_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y9GjUfwQ0GnCSaVq3jgUuTkEqQvHp1Vu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error # to be used alongside root_mean_squared_error
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv("data_fire_resistance.csv")
df

# Initialize label encoders
label_encoders = {
    'structural_type': LabelEncoder(),
    'construction_material': LabelEncoder(),
    'fire_load_type': LabelEncoder(),
    'paint': LabelEncoder()
}

# Fit the encoders with the data and transform the data
df['structural_type'] = label_encoders['structural_type'].fit_transform(df['structural_type'])
df['construction_material'] = label_encoders['construction_material'].fit_transform(df['construction_material'])
df['fire_load_type'] = label_encoders['fire_load_type'].fit_transform(df['fire_load_type'])
df['paint'] = label_encoders['paint'].fit_transform(df['paint'])

# Save the fitted encoders to a file
with open('label_encoders.pkl', 'wb') as encoders_file:
    pickle.dump(label_encoders, encoders_file)

# Display the transformed DataFrame
df

df.info()

# Define features and target variable
x = df.drop(columns=["fire_resistance"])  # Features
y = df["fire_resistance"]  # Target
# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

#Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=1000, max_depth=10, min_samples_split=5, min_samples_leaf=5, random_state=42)
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)
y_pred

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")


# Saving the model with pickle
with open('fire_model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('fire_model.pkl', 'rb') as f:
    model = pickle.load(f)

model



