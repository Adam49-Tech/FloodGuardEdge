import numpy as np
import joblib
# Load the trained model
model = joblib.load('processed/flood_model.pkl')
# Load rainfall and elevation arrays
rainfall_array = np.load('processed/rainfall_array.npy')
elevation_array = np.load('processed/elevation_array.npy')
# Flatten the arrays to 1D
rainfall_flat = rainfall_array.flatten()
elevation_flat = elevation_array.flatten()
# Stack them to create feature matrix
X = np.stack((rainfall_flat, elevation_flat), axis=1)
# Predict flood risk
if model.predict_proba(X).shape[1] == 1:
    prediction = model.predict(X)
else:
    prediction = model.predict_proba(X)[:, 1]
# Reshape back to original map shape
prediction_map = prediction.reshape(rainfall_array.shape)
# Save the prediction map
np.save('processed/flood_risk_prediction.npy', prediction_map)
print('Flood risk prediction saved to: processed/flood_risk_prediction.npy')