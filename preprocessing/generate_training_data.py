import rasterio
import numpy as np
import pandas as pd
import random
import os
def extract_training_data(raster_path, output_csv, num_samples=1000):
    with rasterio.open(raster_path) as src:
        rain = src.read(1)
        elev = src.read(2)
    # Get valid pixel indices (where both values are not nan or nodata)
    valid_mask = (~np.isnan(rain)) & (~np.isnan(elev)) & (rain != src.nodata)
    coords = np.column_stack(np.where(valid_mask))
    if len(coords) < num_samples:
        print(f"⚠️ Only {len(coords)} valid samples found — reducing sample size.")
        num_samples = len(coords)
    sampled_coords = random.sample(list(coords), num_samples)
    data = []
    for row, col in sampled_coords:
        rain_val = rain[row, col]
        elev_val = elev[row, col]
        # For this demo: label = 1 if rainfall > threshold and elevation < threshold
        label = 1 if (rain_val > 100 and elev_val < 200) else 0
        data.append([rain_val, elev_val, label])
    df = pd.DataFrame(data, columns=["rainfall", "elevation", "flood_risk"])
    df.to_csv(output_csv, index=False)
    print(f"✅ Training data saved to: {output_csv}")
if __name__ == "__main__":
    raster_path = "processed/stacked_data.tif"
    output_csv = "processed/training_data.csv"
    extract_training_data(raster_path, output_csv, num_samples=1000)