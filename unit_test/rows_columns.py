import geopandas as gpd
import matplotlib.pyplot as plt

def plot_world_map():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    continent_borders = world.dissolve(by='continent')
    
    world_rows, world_columns = world.shape
    print(f"The 'world' GeoDataFrame has {world_rows} rows and {world_columns} columns.")
    

    continent_borders_rows, continent_borders_columns = continent_borders.shape
    print(f"The 'continent_borders' GeoDataFrame has {continent_borders_rows} rows and {continent_borders_columns} columns.")
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    continent_borders.boundary.plot(ax=ax, linewidth=1, color='black')
    
    ax.set_title("World Map with Continents")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.show()
    
    return world, continent_borders, fig, ax

# Run the function
plot_world_map()
