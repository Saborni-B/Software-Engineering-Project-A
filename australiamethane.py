import geopandas as gpd
import matplotlib.pyplot as plt
from sentinelsat import SentinelAPI

username = "s5pguest"
pwd = "s5pguest"
api_url = "https://s5phub.copernicus.eu/dhus"

api = SentinelAPI(username, pwd, api_url, show_progressbars=True, timeout=60)

# Load the world dataset from geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Australia polygon
australia = world[world['name'] == 'Australia']
australia_geom = australia.geometry.values[0]

# Query Sentinel-5P data Australia
products = api.query(australia_geom, date=('20201216', '20230317'), platformname='Sentinel-5P', producttype='L2__CH4___')

api.download_all(products, '/Users/ud/Documents')

methane_data = gpd.read_file('/Users/ud/Documents')

world.plot()

methane_data.plot(ax=plt.gca(), color='red')


plt.show()
