import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.warp import reproject, calculate_default_transform
def read_raster(fp):
    with rasterio.open(fp) as src:
        data = src.read(1)
        profile = src.profile
    return data, profile
def reproject_match(source_fp, target_profile):
    with rasterio.open(source_fp) as src:
        dst_array = np.empty((target_profile['height'], target_profile['width']), dtype=np.float32)
        reproject(
            source=rasterio.band(src, 1),
            destination=dst_array,
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=target_profile['transform'],
            dst_crs=target_profile['crs'],
            resampling=Resampling.bilinear
        )
    return dst_array
def stack_and_save(rain_fp, elev_fp, output_fp):
    # Read rainfall raster (reference)
    rain, rain_profile = read_raster(rain_fp)
    # Reproject and resample elevation to match rainfall
    elev = reproject_match(elev_fp, rain_profile)
    print("Rainfall shape:", rain.shape)
    print("Elevation shape:", elev.shape)
    if rain.shape != elev.shape:
        raise ValueError("Shapes do not match after resampling!")
    # Stack the two arrays
    stacked = np.stack([rain, elev])
    # Update metadata for 2-band output
    rain_profile.update({
        'count': 2,
        'dtype': 'float32'
    })
    with rasterio.open(output_fp, 'w', **rain_profile) as dst:
        dst.write(stacked.astype('float32'))
if __name__ == "__main__":
    rain_fp = "CHIRPS_AprilOct2024.tif"
    elev_fp = "SRTM_Elevation_Reduced.tif"
    output_fp = "processed/stacked_data.tif"
    stack_and_save(rain_fp, elev_fp, output_fp)