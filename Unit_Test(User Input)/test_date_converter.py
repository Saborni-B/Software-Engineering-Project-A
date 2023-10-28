
from datetime import datetime
import unittest

def convert_format_date(input_date):
    correct_formats = ["%d %m %Y", "%Y %m %d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y", "%Y-%m-%d"]
    
    for format_str in correct_formats:
        try:
            date_obj = datetime.strptime(input_date, format_str)
            formatted_date = date_obj.strftime("%Y-%m-%d")
            return formatted_date
        except ValueError:
            pass
    
    raise ValueError("Invalid data format")


class TestConvertFormatDate(unittest.TestCase):

  
    def test_date_components(self):
        self.assertEqual(convert_format_date("2021 12 31"), "2021-12-31")

    def test_converted_format(self):
        self.assertEqual(convert_format_date("31 12 2021"), "2021-12-31")

    def test_invalid_date_variation(self):
        with self.assertRaises(ValueError):
            convert_format_date("31-12-21")

    def test_invalid_text_input(self):
        with self.assertRaises(ValueError):
            convert_format_date("invalid_date")

    def test_different_approved_formats(self):
        self.assertEqual(convert_format_date("31/12/2021"), "2021-12-31")
        self.assertEqual(convert_format_date("2021-12-31"), "2021-12-31")

if __name__ == "__main__":
    unittest.main()
