import streamlit as st
import numpy as np
import rasterio
import matplotlib.pyplot as plt
# Set up Streamlit page
st.set_page_config(page_title="FloodGuardEdge - Flood Risk Prediction", layout="wide")
st.title("🌊 FloodGuardEdge - Flood Risk Prediction App")
st.write("An interactive tool to visualize predicted flood risks based on rainfall and elevation data.")
# Load flood risk prediction
flood_risk = np.load('processed/flood_risk_prediction.npy')
# Load rainfall data and handle NaN values
rainfall_array = np.load('processed/rainfall_array.npy')
rainfall_array = np.nan_to_num(rainfall_array, nan=0.0)  # Replace NaN with 0.0
# Simulate a region map (replace with real data when available)
region_map = np.random.choice(['North Central', 'North East', 'North West', 'South East', 'South South', 'South West'], size=flood_risk.shape)
# Sidebar Filters
st.sidebar.header("🛠️ Filter Options")
# Safe Rainfall Threshold Slider
min_rainfall = float(np.nanmin(rainfall_array))
max_rainfall = float(np.nanmax(rainfall_array))
if min_rainfall == max_rainfall:
    st.warning("Rainfall values are constant or missing. Slider disabled.")
    rainfall_threshold = min_rainfall
else:
    rainfall_threshold = st.sidebar.slider(
        'Select Rainfall Threshold (mm)',
        min_value=min_rainfall,
        max_value=max_rainfall,
        value=(min_rainfall + max_rainfall) / 2
    )
# Region Filter
region = st.sidebar.selectbox("Select Region (Geopolitical Zone)", options=['All', 'North Central', 'North East', 'North West', 'South East', 'South South', 'South West'])
# Severity Filter
severity = st.sidebar.selectbox("Select Flood Severity", options=['All', 'Low', 'Medium', 'High'])
# Apply Rainfall Threshold
filtered_map = np.where(rainfall_array >= rainfall_threshold, flood_risk, 0)
# Apply Region Filter
if region != 'All':
    region_mask = (region_map == region)
    filtered_map = np.where(region_mask, filtered_map, 0)
# Apply Severity Filter
if severity != 'All':
    if severity == 'Low':
        filtered_map = np.where((filtered_map > 0) & (filtered_map <= 0.3), filtered_map, 0)
    elif severity == 'Medium':
        filtered_map = np.where((filtered_map > 0.3) & (filtered_map <= 0.6), filtered_map, 0)
    elif severity == 'High':
        filtered_map = np.where(filtered_map > 0.6, filtered_map, 0)
# Display the filtered map
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(filtered_map, cmap='YlOrRd', interpolation='none')
fig.colorbar(cax, ax=ax, label='Flood Risk Level')
ax.set_title("Predicted Flood Risk Map (Filtered)")
st.pyplot(fig)
# Footer
st.write("© 2025 FloodGuardEdge - Developed by Adam49-Tech")