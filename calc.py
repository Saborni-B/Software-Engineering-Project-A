def add(x, y):
    #Add function
    return x + y

def subtract(x, y):
    #Subtract function
    return x - y

def multiply(x, y):
    #Multiply function
    return x * y

def divide(x, y):
    #Divide function 
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y


#Testing the add function
print(add(10, 5))
#Testing the divide (ValueError)
#print(divide(2, 0))


import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        
