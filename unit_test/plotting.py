import geopandas as gpd
import matplotlib.pyplot as plt

def plot_world_map():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    continent_borders = world.dissolve(by='continent')
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    continent_borders.boundary.plot(ax=ax, linewidth=1, color='black')
    world.boundary.plot(ax=ax, linewidth=0.5, color='black')
    ax.set_title("World Map with Continents and Countries")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
