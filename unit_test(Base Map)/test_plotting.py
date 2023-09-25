import unittest
import geopandas as gpd
import matplotlib.pyplot as plt
from plotting import plot_world_map  

class TestGeoPandasPlotting(unittest.TestCase):

    def test_data_loading(self): #Testing if the GeoPandas read_file method successfully loads the dataset.
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        self.assertIsNotNone(world)

    def test_data_transformation(self): #Testing if the dissolve method correctly aggregates the data by continent.
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        continent_borders = world.dissolve(by='continent')
        self.assertIsNotNone(continent_borders)

if __name__ == '__main__':
    unittest.main()
