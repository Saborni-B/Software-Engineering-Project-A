from sentinelsat import SentinelAPI
from shapely.geometry import Polygon
from datetime import date

# Your Copernicus Open Access Hub credentials
user = 'rafayet44'
password = '12345678'

# Connecting to the API
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

# Define area of interest (in this case, a rough bounding box for Australia)
footprint = Polygon([(110, -45), (160, -45), (160, -10), (110, -10)])

# Define date range
start_date = date(2022, 1, 1)
end_date = date(2022, 12, 31)

# Query Copernicus Hub for Sentinel-5P methane data
products = api.query(footprint,
                     date=(start_date, end_date),
                     platformname='Sentinel-5',
                     processinglevel='Level-2',
                     producttype='Methane')

# Print product information
for product_id, product_info in products.items():
    print(f"Product ID: {product_id}")
    print(f"Title: {product_info['title']}")
    print(f"Date: {product_info['beginposition']} to {product_info['endposition']}")
    print("--------------------------------------------------")

downloaded_files = api.download_all(products)
