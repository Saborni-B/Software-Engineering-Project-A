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
#x//y does not raise an error when 'y' is equal to 0 because integer division'//' in Python handles division by zero differently than regular division'/'