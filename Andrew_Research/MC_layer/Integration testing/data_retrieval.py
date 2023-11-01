import matplotlib.pyplot as plt
import netCDF4 as nc4
import xarray as xr
import fsspec
import numpy as np
import xarray as xr
import planetary_computer
import pystac_client
import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, time
import json

# Initialize PySTAC client for data query
planetary_computer.set_subscription_key("c27669c4bdec434d804e2bd738cb16fc")
catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

#The acceptable formats are dd mm YYYYY, YYYY mm dd, dd-mm-YYYY, YYYY-mm-dd, dd/mm/YYYY, YYYY/mm/dd
start_date = "2023 08 10"
end_date = "25 08 2023"
region = [174.563615, -36.893762, 174.860246, -36.717901] #Auckland NZ

# Function to convert date format 
def convert_format_date(input_date):
    correct_formats = ["%d %m %Y", "%Y %m %d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y", "%Y-%m-%d"]
    
    for format_str in correct_formats:
        try:
            date_obj = datetime.strptime(input_date, format_str)
            formatted_date = date_obj.strftime("%Y-%m-%d")
            return formatted_date
        except ValueError: # Raised if input format is not compatible with set standard 
            pass
    
    raise ValueError("Invalid data format")

# Convert user start date format
try:
    start_date = convert_format_date(start_date)
except ValueError:
    print("Invalid start date format. Please check the acceptable formats")
            
# Convert user end date format
try:
    end_date = convert_format_date(end_date)
except ValueError:
    print("Invalid end date format. Please check the acceptable formats")

date_period = start_date + "/" + end_date 
print(date_period)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')) # Get geopandas in-built naturalearth_lowres dataset

def search_catalog(region, date_period):
    search_parameters = {
        "collections": "sentinel-5p-l2-netcdf",
        "datetime": date_period,
        "query": {"s5p:processing_mode": {"eq": "OFFL"}, "s5p:product_name": {"eq": "ch4"}},
    }
   
    #bbox input
    if isinstance(region, list) and len(region) == 4:
        min_long, min_lat, max_long, max_lat = region
        #-180 to 180 for longitudes, -90 to 90 for latitudes
        long = all(-180 <= coordinates <= 180 for coordinates in [min_long, max_long]) 
        lat = all(-90 <= coordinates <= 90 for coordinates in [min_lat, max_lat])
        
        if long and lat:
            search_parameters["bbox"] = region
        elif not long:
            raise ValueError("Invalid longitudes in bbox")
        elif not lat:
            raise ValueError("Invalid latitudes in bbox")
        else:
            raise ValueError("Invalid coordinates in bbox")
        
    else:
        # Extract the coordinates of specified country and load into a JSON object 
        ROI = world[world["name"] == region]
        gjson = json.loads(ROI.to_json())
        coordinates = gjson["features"][0]["geometry"]["coordinates"]
        
        if not isinstance(coordinates, list): 
            coordinates = [coordinates]    
                         
        #MultiPolygon is used to represent multiple polygons bbox and country     
        search_parameters["intersects"] = {
            "type": "MultiPolygon", 
            "coordinates": coordinates
        }
        
    search = catalog.search(**search_parameters)
    items = search.item_collection()

    return items

# Use search_catalog function with a single variable "region" for bbox and country name
result = search_catalog(region=region, date_period=date_period)

# Print the result
print(f"Number of items for input: {len(result)}")

for item in result:
    print(item)


