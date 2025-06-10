import rasterio
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
def show_flood_map(prediction_path, output_image):
    with rasterio.open(prediction_path) as src:
        flood_map = src.read(1)
    cmap = ListedColormap(["lightgrey", "red"])  # 0 = no risk, 1 = risk
    bounds = [0, 0.5, 1]
    norm = BoundaryNorm(bounds, cmap.N)
    plt.figure(figsize=(10, 8))
    plt.title("Predicted Flood Risk Map")
    im = plt.imshow(flood_map, cmap=cmap, norm=norm)
   
    cbar = plt.colorbar(im, ticks=[0, 1])
    cbar.ax.set_yticklabels(["No Risk (0)", "Flood Risk (1)"])
    plt.axis("off")
   
    # Save to file
    plt.savefig(output_image)
    print(f"🖼️ Flood map image saved as: {output_image}")
if __name__ == "__main__":
    prediction_path = "processed/flood_risk_map.tif"
    output_image = "processed/flood_map_visual.png"
    show_flood_map(prediction_path, output_image)