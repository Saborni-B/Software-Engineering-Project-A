import ipytest
#import unittest
#from datetime import user_input
import user_input.ipynb

def test_addition():
    assert add(2, 3) == 5, "Test failed: 2 + 3 should be 5"
    assert add(-1, 1) == 0, "Test failed: -1 + 1 should be 0"
    assert add(0, 0) == 0, "Test failed: 0 + 0 should be 0"

#class TestDateTime(unittest.TestCase):
 #   def test_date(self):
        #if user_start_date == "%d/%m/%Y"
  #      self.assertIsInstance(time_stamp,str, msg="%s not a string" %time_stamp)
   #     self.assertIsInstance(datetime.strptime(time_stamp, "%d/%m/%Y"), datetime.datetime)

    #    with self.assertRaises(ValueError):
     #       user_end_date != "%d/%m/%Y"
    
    #def test_time(user_start_time, user_end_time):
        
#if __name__ == '__main__':
 #   unittest.main()