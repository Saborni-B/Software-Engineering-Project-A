import unittest
from dates import convert_format_date

class TestConvertFormatDate(unittest.TestCase):

    def test_date_components(self):
        self.assertEqual(convert_format_date("2022 10 08", "%Y %m %d", "%Y-%m-%d"), "2022-10-08")
        self.assertEqual(convert_format_date("", "%Y %m %d", "%Y-%m-%d"), "Not provided")
        self.assertEqual(convert_format_date("123456", "%Y %m %d", "%Y-%m-%d"), "Not provided")

    def test_output_format(self):
        self.assertEqual(convert_format_date("2022 10 08", "%Y %m %d", "%Y-%m-%d"), "2022-10-08")
        self.assertNotEqual(convert_format_date("2022 10 08", "%Y %m %d", "%Y-%m-%d"), "08-10-2022")

if __name__ == "__main__":
    unittest.main()
