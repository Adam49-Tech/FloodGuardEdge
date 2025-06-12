import streamlit as st
import numpy as np
import geopandas as gpd
import rasterio
import matplotlib.pyplot as plt
# Set up Streamlit page
st.set_page_config(page_title="FloodGuardEdge - Flood Risk Prediction", layout="wide")
st.title("🌊 FloodGuardEdge - Flood Risk Prediction App")
st.write("An interactive tool to visualize predicted flood risks based on rainfall and elevation data.")
# Load flood risk GeoTIFF with geospatial reference
flood_risk_path = 'processed/flood_risk_map.tif'
with rasterio.open(flood_risk_path) as src:
    flood_risk = src.read(1)
    flood_risk_bounds = src.bounds
    flood_risk_extent = [flood_risk_bounds.left, flood_risk_bounds.right, flood_risk_bounds.bottom, flood_risk_bounds.top]
# Load rainfall data and handle NaN values
rainfall_array = np.load('processed/rainfall_array.npy')
rainfall_array = np.nan_to_num(rainfall_array, nan=0.0)  # Replace NaN with 0.0
# Load Nigeria shapefile using GeoPandas
nigeria_shape = gpd.read_file('shapefiles/gadm41_NGA_1.shp')
# Simulate a region map (replace with real region map later)
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
# Display the flood risk map with Nigeria boundary
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(filtered_map, cmap='YlOrRd', interpolation='none', extent=flood_risk_extent, origin='upper')
fig.colorbar(cax, ax=ax, label='Flood Risk Level')
# Plot Nigeria shapefile boundary
nigeria_shape.boundary.plot(ax=ax, edgecolor='black', linewidth=1)
ax.set_title("Predicted Flood Risk Map (Georeferenced)")
st.pyplot(fig)
import pandas as pd
import io
# Sidebar Header for Download
st.sidebar.header("📥 Download Options")
# Progress Spinner for Download Preparation
with st.spinner('Preparing download...'):
    # Convert the filtered map to a DataFrame
    filtered_df = pd.DataFrame(filtered_map)
    # Convert DataFrame to CSV
    csv = filtered_df.to_csv(index=False)
    csv_bytes = csv.encode()
# Download Button
st.sidebar.download_button(
    label="Download Filtered Map as CSV",
    data=csv_bytes,
    file_name="filtered_flood_risk_map.csv",
    mime="text/csv"
)
st.success('Download ready!')
# Footer
st.write("© 2025 FloodGuardEdge - Developed by Adam49-Tech")