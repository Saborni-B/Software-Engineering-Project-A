from datetime import datetime
import json
import unittest
import geopandas as gpd


def search_catalog(region, date_period):
    search_parameters = {
        "collections": "sentinel-5p-l2-netcdf",
        "datetime": date_period,
        "query": {"s5p:processing_mode": {"eq": "OFFL"}, "s5p:product_name": {"eq": "ch4"}},
    }
    if isinstance(region, list) and len(region) == 4:
        min_long, min_lat, max_long, max_lat = region
        long = all(-180 <= coordinates <=
                   180 for coordinates in [min_long, max_long])
        lat = all(-90 <= coordinates <=
                  90 for coordinates in [min_lat, max_lat])

        if long and lat:
            search_parameters["bbox"] = region
        elif not long:
            raise ValueError("Invalid longitudes in bbox")
        elif not lat:
            raise ValueError("Invalid latitudes in bbox")
        else:
            raise ValueError("Invalid coordinates in bbox")
    else:
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        ROI = world[world["name"] == region]
        gjson = json.loads(ROI.to_json())
        coordinates = gjson["features"][0]["geometry"]["coordinates"]

        if not isinstance(coordinates, list):
            coordinates = [coordinates]
        search_parameters["intersects"] = {
            "type": "MultiPolygon",
            "coordinates": coordinates
        }
    return search_parameters


class TestBboxAndCountryName(unittest.TestCase):

    # Testing valid coordinates
    def test_valid_bounding_box(self):
        # Swinburne University Hawthorn campus
        region = [145.030035, -37.828963, 145.042158, -37.815471]
        date_period = "2022-09-01/2022-09-30"
        result = search_catalog(region, date_period)
        self.assertEqual(result["bbox"], region)

    # Testing invalid coordinates
    def test_invalid_bounding_box(self):
        region = [190, -90, 200, -100]
        date_period = "2022-09-01/2022-09-30"
        with self.assertRaises(ValueError):
            search_catalog(region, date_period)

    # Testing invalid latitude
    def test_invalid_latitude(self):
        region = [145.030035, -97.828963, 145.042158, -37.815471]
        date_period = "2022-09-01/2022-09-30"
        with self.assertRaises(ValueError):
            search_catalog(region, date_period)

    # Testing invalid longitude
    def test_invalid_longitude(self):
        region = [245.030035, -37.828963, 145.042158, -37.815471]
        date_period = "2022-09-01/2022-09-30"
        with self.assertRaises(ValueError):
            search_catalog(region, date_period)

    # Testing valid country name
    def test_valid_country_name(self):
        region = "Japan"
        date_period = "2022-10-01/2022-10-30"
        result = search_catalog(region, date_period)
        self.assertEqual(result["intersects"]["type"], "MultiPolygon")

    # Testing invalid country name
    def Test_invalid_country_name(self):
        region = "111"
        date_period = "2022-10-01/2022-10-30"
        with self.assertRaises(ValueError):
            search_catalog(result["intersects"]["type"], "MultiPolygon")


if __name__ == '__main__':
    unittest.main()
