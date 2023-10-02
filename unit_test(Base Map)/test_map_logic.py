# test_map_logic.py
import unittest
from map_logic import plot_world_map

class TestMapLogic(unittest.TestCase):

    def test_world_dataframe_shape(self):
        world, _, _, _ = plot_world_map()
        expected_row_count = 177  
        expected_column_count = 6  
        self.assertEqual(world.shape, (expected_row_count, expected_column_count))

    def test_continent_dataframe_shape(self):
        _, continent_borders, _, _ = plot_world_map()
        expected_row_count = 8 
        expected_column_count = 5  
        self.assertEqual(continent_borders.shape, (expected_row_count, expected_column_count))

if __name__ == '__main__':
    unittest.main()
