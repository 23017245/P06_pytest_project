def test_assert_true():
    assert True

def test_assert_false():
    assert False

class Calculator:
    def __init__(self,add,subtract,multiply,divide):
        self.add = add
        self.subtract = subtract
        self.multiply = multiply
        self.divide = divide

    def add(self, a, b):
        return a + b	
    
    def subtract(self, a, b):
        return a - b	

    def multiply(self, a, b):
        return a * b	  
    
    def divide(self, a, b):
        return a / b