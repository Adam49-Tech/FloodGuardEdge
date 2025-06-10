import streamlit as st
from PIL import Image
import os
import numpy as np
import rasterio
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.pyplot as plt
# Set up the Streamlit page
st.set_page_config(page_title="FloodGuardEdge", layout="centered")
st.title("🌊 FloodGuardEdge")
st.markdown("""
Welcome to **FloodGuardEdge** – a predictive flood risk monitoring tool using satellite data and machine learning.
🚀 This prototype visualizes areas at risk of flooding in Nigeria based on rainfall and elevation data.
""")
# Load the predicted flood map
map_path = os.path.join("processed", "flood_risk_map.tif")
if os.path.exists(map_path):
    with rasterio.open(map_path) as src:
        flood_map = src.read(1)
    # State options
    selected_state = st.selectbox(
        "Select a state to highlight:",
        ("Benue", "Abuja", "Niger", "Lagos", "Kogi", "Bayelsa", "Anambra", "Borno", "All States")
    )
    st.write(f"🗺️ Showing flood risk for: **{selected_state}**")
    # Rainfall threshold slider
    threshold = st.slider(
        "Set minimum rainfall threshold to simulate flood (mm)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )
    # Apply rainfall threshold
    filtered_map = np.where(flood_map >= threshold, 1, 0)
    # Display the filtered map
    cmap = ListedColormap(["lightgrey", "red"])
    bounds = [0, 0.5, 1]
    norm = BoundaryNorm(bounds, cmap.N)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f"Flood Risk Map – Threshold: {threshold}")
    im = ax.imshow(filtered_map, cmap=cmap, norm=norm)
    ax.axis('off')
    cbar = plt.colorbar(im, ticks=[0, 1])
    cbar.ax.set_yticklabels(["No Risk", "Flood Risk"])
    st.pyplot(fig)
else:
    st.warning("Flood risk map not found. Please run the model pipeline first.")