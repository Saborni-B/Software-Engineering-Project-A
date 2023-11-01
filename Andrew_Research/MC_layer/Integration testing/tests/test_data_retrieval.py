import pytest
import datetime

from data_retrieval import convert_format_date, search_catalog


def test_data_retrieval():
    region = [174.563615, -36.893762, 174.860246, -36.717901]
    start_date_input = "2023 09 15"
    end_date_input = "2023 09 18"
    
    start_date_str = convert_format_date(start_date_input)
    end_date_str = convert_format_date(end_date_input)
    
    date_period = start_date_str + "/" + end_date_str
    
    items = search_catalog(region=region, date_period=date_period)
    
    for item in items:
        
        item = str(item)
            
        assert ("S5P_L2_CH4____" in item) is True
        
        start_index = item.find("<Item id=S5P_L2_CH4____")
        # Extract the date portion from the item string
        date_str = item[start_index + len("<Item id=S5P_L2_CH4____"):
                        start_index + len("<Item id=S5P_L2_CH4____") + 8]

        # Convert the date string to a datetime object
        date_format = "%Y%m%d"
        item_date = datetime.datetime.strptime(date_str, date_format)
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        
        assert (start_date <= item_date <= end_date) is True




    
    


