import numpy as np
import rasterio
# Load stacked data
with rasterio.open('processed/stacked_data.tif') as src:
    stacked_data = src.read()
# Separate rainfall and elevation arrays
rainfall_array = stacked_data[0]
elevation_array = stacked_data[1]
# Save as .npy files
np.save('processed/rainfall_array.npy', rainfall_array)
np.save('processed/elevation_array.npy', elevation_array)
print("Rainfall and elevation arrays have been saved successfully.")