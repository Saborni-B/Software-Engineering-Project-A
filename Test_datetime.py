import unittest
from datetime import datetime, time
import user_input


class TestDateTime(unittest.TestCase):
    def test_date(user_start_date, user_end_date):
        #if user_start_date == "%d/%m/%Y"
        self.assertIsInstance(time_stamp,str, msg="%s not a string" %time_stamp)
        self.assertIsInstance(datetime.strptime(time_stamp, "%d/%m/%Y"), datetime.datetime)

        with self.assertRaises(ValueError):
            user_end_date != "%d/%m/%Y"
    
    #def test_time(user_start_time, user_end_time):
        
if __name__ == '__main__':
    unittest.main()