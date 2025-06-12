import streamlit as st
import numpy as np
import geopandas as gpd
import rasterio
import matplotlib.pyplot as plt
import pandas as pd
import io
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
rainfall_array = np.nan_to_num(rainfall_array, nan=0.0)
# Load Nigeria shapefile using GeoPandas
nigeria_shape = gpd.read_file('shapefiles/gadm41_NGA_1.shp')
# Extract list of states
state_names = nigeria_shape['NAME_1'].unique().tolist()
state_names.insert(0, 'All')  # Add 'All' option
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
# State Filter
selected_state = st.sidebar.selectbox("Select State", options=state_names)
# Severity Filter
severity = st.sidebar.selectbox("Select Flood Severity", options=['All', 'Low', 'Medium', 'High'])
# Apply Rainfall Threshold
filtered_map = np.where(rainfall_array >= rainfall_threshold, flood_risk, 0)
# Apply Severity Filter
if severity != 'All':
    if severity == 'Low':
        filtered_map = np.where((filtered_map > 0) & (filtered_map <= 0.3), filtered_map, 0)
    elif severity == 'Medium':
        filtered_map = np.where((filtered_map > 0.3) & (filtered_map <= 0.6), filtered_map, 0)
    elif severity == 'High':
        filtered_map = np.where(filtered_map > 0.6, filtered_map, 0)
# Sidebar Header for Download Options
st.sidebar.header("📥 Download Options")
# Progress Spinner for Map Processing
with st.spinner('Processing flood risk map...'):
    if selected_state != 'All':
        selected_shape = nigeria_shape[nigeria_shape['NAME_1'] == selected_state]
        fig, ax = plt.subplots(figsize=(10, 8))
        cax = ax.imshow(filtered_map, cmap='YlOrRd', interpolation='none', extent=flood_risk_extent, origin='upper')
        fig.colorbar(cax, ax=ax, label='Flood Risk Level')
        # Plot selected state boundary
        selected_shape.boundary.plot(ax=ax, edgecolor='black', linewidth=1)
        ax.set_title(f"Flood Risk Map - {selected_state}")
        st.pyplot(fig)
    else:
        fig, ax = plt.subplots(figsize=(10, 8))
        cax = ax.imshow(filtered_map, cmap='YlOrRd', interpolation='none', extent=flood_risk_extent, origin='upper')
        fig.colorbar(cax, ax=ax, label='Flood Risk Level')
        # Plot entire Nigeria boundary
        nigeria_shape.boundary.plot(ax=ax, edgecolor='black', linewidth=1)
        ax.set_title("Flood Risk Map - Nigeria")
        st.pyplot(fig)
st.success('Map rendered successfully!')
# Prepare filtered map for CSV download
filtered_df = pd.DataFrame(filtered_map)
csv = filtered_df.to_csv(index=False)
csv_bytes = csv.encode()
# CSV Download Button
st.sidebar.download_button(
    label="Download Filtered Map as CSV",
    data=csv_bytes,
    file_name="filtered_flood_risk_map.csv",
    mime="text/csv"
)
# Save the map as a PNG in memory
img_buffer = io.BytesIO()
fig.savefig(img_buffer, format='png')
img_buffer.seek(0)
# PNG Download Button
st.sidebar.download_button(
    label="Download Flood Risk Map as PNG",
    data=img_buffer,
    file_name="flood_risk_map.png",
    mime="image/png"
)
# Footer
st.write("© 2025 FloodGuardEdge - Developed by Adam49-Tech")