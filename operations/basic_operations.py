class BasicOperations:
    """Handles basic arithmetic operations"""

    @staticmethod
    def add(a: float, b: float) -> float:
        """ADD TWO NUMBERS"""
        return a + b
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """ Subtract two numbers"""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b"""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
