import rasterio
import numpy as np
import joblib
from rasterio.transform import from_origin
def predict_flood_risk(input_raster, model_path, output_raster):
    # Load the trained model
    model = joblib.load(model_path)
    # Open stacked raster
    with rasterio.open(input_raster) as src:
        rain = src.read(1)
        elev = src.read(2)
        profile = src.profile
    # Flatten the arrays
    rows, cols = rain.shape
    rain_flat = rain.flatten()
    elev_flat = elev.flatten()
    # Stack features
    X = np.column_stack((rain_flat, elev_flat))
    # Mask invalid pixels
    valid_mask = (~np.isnan(rain_flat)) & (~np.isnan(elev_flat)) & (rain_flat != src.nodata)
    predictions = np.zeros_like(rain_flat, dtype=np.uint8)
    predictions[valid_mask] = model.predict(X[valid_mask])
    # Reshape to original image shape
    prediction_map = predictions.reshape((rows, cols))
    # Save predicted flood map
    profile.update(dtype=rasterio.uint8, count=1)
    with rasterio.open(output_raster, "w", **profile) as dst:
        dst.write(prediction_map, 1)
    print(f"✅ Flood prediction map saved to: {output_raster}")
if __name__ == "__main__":
    input_raster = "processed/stacked_data.tif"
    model_path = "processed/flood_model.pkl"
    output_raster = "processed/flood_risk_map.tif"
    predict_flood_risk(input_raster, model_path, output_raster)