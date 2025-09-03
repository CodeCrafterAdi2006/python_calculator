import math
class AdvancedOperations:
    """Handles advanced mathematical operations"""
    @staticmethod
    def power(base: float, exponent: float)-> float:
        """Raise base to the power of exponent"""
        return base ** exponent

    @staticmethod
    def square_root(number: float)-> float:
        """Calculate square root"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(number)

    @staticmethod
    def factorial(number: int) -> int:
        """Calculate factorial"""
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers")

        if number == 0:
            return 1
        return number * AdvancedOperations.factorial(number - 1)

    @staticmethod
    def percentage(number: float, percent: float) -> float:
        """Calculate percentage"""
        return (number * percent) / 100