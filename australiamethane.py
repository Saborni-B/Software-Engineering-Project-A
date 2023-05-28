from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import datetime

import geopandas as gpd
from shapely.geometry import mapping

api = SentinelAPI('s5pguest', 's5pguest', 'https://s5phub.copernicus.eu/dhus')
product_type = 'L2__CH4___'

# Load the GeoJSON file of Australia
countries_geojson_file = '/Users/ud/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
countries_gdf = gpd.read_file(countries_geojson_file)

australia_gdf = countries_gdf[countries_gdf['ADMIN'] == 'Australia']
australia_geometry = australia_gdf.geometry.iloc[0]
geometry_dict = mapping(australia_geometry)
geometry_wkt = geojson_to_wkt(geometry_dict)

date_range = (datetime(2022, 3, 1), datetime(2022, 4, 20))

products = api.query(geometry=geometry_wkt, date=date_range, producttype=product_type)
