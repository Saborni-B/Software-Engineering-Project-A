#import ipytest
import unittest
import nbimporter
import user_input as eg


class TestSample(unittest.TestCase):
        
    def test_add(self):
      expected_state = 4
      returned_state = eg.add(1, 2)
      self.assertEqual(expected_state, returned_state)
        
        # Check if an exception of type ValueError is raised
        #if returned_state != 4:
         #   self.assertIsInstance(ValueError)
      with self.assertRaises(ValueError):
        eg.add("string", 2)
        
if __name__ == '__main__':
    unittest.main()
#unittest.main(argv=[''], verbosity=2, exit=False)

 
#import testbook

#@testbook.testbook('Users/jenni/Documents/GitHub/Software-Engineering-Project-A/user_input.ipynb', execute=True)
#def test_func(tb):
 #   func = tb.ref("func")

  #  assert func(1, 2) == 3   
#class TestDateTime(unittest.TestCase):
 #   def test_date(self):
        #if user_start_date == "%d/%m/%Y"
  #      self.assertIsInstance(time_stamp,str, msg="%s not a string" %time_stamp)
   #     self.assertIsInstance(datetime.strptime(time_stamp, "%d/%m/%Y"), datetime.datetime)

    #    with self.assertRaises(ValueError):
     #       user_end_date != "%d/%m/%Y"
    
    #def test_time(user_start_time, user_end_time):
        
