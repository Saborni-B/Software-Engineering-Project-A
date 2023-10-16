

# Function to search the product by bbox and country
def search_catalog(Region, date_period):
    search_parameters = {
        "collections": "sentinel-5p-l2-netcdf",
        "datetime": date_period,
        "query": {"s5p:processing_mode": {"eq": "OFFL"}, "s5p:product_name": {"eq": "ch4"}},
    }
   
    #bbox input
    if isinstance(Region, list) and len(Region) == 4:
        min_long, min_lat, max_long, max_lat = Region
        #-180 to 180 for longitudes, -90 to 90 for latitudes
        long = all(-180 <= coordinates <= 180 for coordinates in [min_long, max_long]) 
        lat = all(-90 <= coordinates <= 90 for coordinates in [min_lat, max_lat])
        
        if long and lat:
            search_parameters["bbox"] = Region
        elif not long:
            raise ValueError("Invalid longitudes in bbox")
        elif not lat:
            raise ValueError("Invalid latitudes in bbox")
        else:
            raise ValueError("Invalid coordinates in bbox")
        
    else:
        # Extract the coordinates of specified country and load into a JSON object 
        ROI = world[world["name"] == Region]
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

# Use search_catalog function with a single variable "Region" for bbox and country name
result = search_catalog(Region=Region, date_period=date_period)

# Print the result
print(f"Number of items for input: {len(result)}")