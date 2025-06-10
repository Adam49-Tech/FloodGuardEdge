import rasterio
import matplotlib.pyplot as plt
def visualize_stacked_raster(filepath):
    with rasterio.open(filepath) as src:
        rain = src.read(1)
        elev = src.read(2)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.set_title('Rainfall (CHIRPS)')
    img1 = ax1.imshow(rain, cmap='Blues')
    fig.colorbar(img1, ax=ax1, shrink=0.5)
    ax2.set_title('Elevation (SRTM)')
    img2 = ax2.imshow(elev, cmap='terrain')
    fig.colorbar(img2, ax=ax2, shrink=0.5)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    visualize_stacked_raster("processed/stacked_data.tif")