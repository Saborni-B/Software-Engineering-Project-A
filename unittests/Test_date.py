from datetime import datetime
import unittest

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

class TestConvertFormatDate(unittest.TestCase):

    #Valid date formats
    def test_date_components(self):
        self.assertEqual(convert_format_date("2021 12 31"), "2021-12-31")
        self.assertEqual(convert_format_date("31 12 2021"), "2021-12-31")
        self.assertEqual(convert_format_date("31/12/2021"), "2021-12-31")
        self.assertEqual(convert_format_date("2021/12/31"), "2021-12-31")
        self.assertEqual(convert_format_date("2021-12-31"), "2021-12-31")
        self.assertEqual(convert_format_date("31-12-2021"), "2021-12-31")

    #Valid date format with different delimiter
    def test_converted_format(self):
        self.assertEqual(convert_format_date("31 12 2021"), "2021-12-31")

    #Valid date variations
    def test_invalid_date_variation(self):
        # Two-digit year format
        with self.assertRaises(ValueError):
            convert_format_date("31-12-21")  
        with self.assertRaises(ValueError):
            convert_format_date("21-12-31") 
        with self.assertRaises(ValueError):
            convert_format_date("31 12 99")  
        with self.assertRaises(ValueError):
            convert_format_date("12/31/21")  
        with self.assertRaises(ValueError):
            convert_format_date("31/12/99")  
        with self.assertRaises(ValueError):
            convert_format_date("12 31 21")  
        with self.assertRaises(ValueError):
            convert_format_date("21 31 12")  

            
    #Invalid date components        
    def test_invalid_date_components(self):
            # Invalid month (13)
        with self.assertRaises(ValueError):
            convert_format_date("2021 13 01")  
            # Invalid day for February
        with self.assertRaises(ValueError):
            convert_format_date("2021 02 31")  
            # Invalid month (00)
        with self.assertRaises(ValueError):
            convert_format_date("2021 00 01") 
            # Invalid day (32)
        with self.assertRaises(ValueError):
            convert_format_date("2021 01 32")  
            # Invalid month and day (00)  
        with self.assertRaises(ValueError):
            convert_format_date("2021 00 00")       
            # Invalid day for September
        with self.assertRaises(ValueError):
            convert_format_date("2021 09 31")  
            
    #Non standard delimiters        
    def test_non_standard_delimiters(self):
        with self.assertRaises(ValueError):
            convert_format_date("2021.12.31")  
        with self.assertRaises(ValueError):
            convert_format_date("2021 12-31") 
    
    # Date with text
    def test_date_with_text(self):
        with self.assertRaises(ValueError):
            convert_format_date("2021-12-31 ABC")  
    
    #Empty input
    def test_empty_string_input(self):
        with self.assertRaises(ValueError):
            convert_format_date("")

    #Non date input
    def test_non_date_input(self):
        with self.assertRaises(ValueError):
            convert_format_date("This is not a date")
            
    #Single digit month and day        
    def test_single_digit_month_day(self):
        self.assertEqual(convert_format_date("5 9 2022"), "2022-09-05")

    #Different correct formats
    def test_different_approved_formats(self):
        self.assertEqual(convert_format_date("31/12/2021"), "2021-12-31")
        self.assertEqual(convert_format_date("2022-12-31"), "2022-12-31")
        self.assertEqual(convert_format_date("05-07-2021"), "2021-07-05")
        self.assertEqual(convert_format_date("2022/02/15"), "2022-02-15")
        self.assertEqual(convert_format_date("2022 09 01"), "2022-09-01")
        
    #Date boundary 
    def test_boundary_values(self):
        # Test with earliest and latest valid dates
        self.assertEqual(convert_format_date("0001 01 01"), "0001-01-01")
        self.assertEqual(convert_format_date("9999 12 31"), "9999-12-31")
        
if __name__ == '__main__':
    unittest.main()
    
#unittest.main(argv=[''], verbosity=2, exit=False)