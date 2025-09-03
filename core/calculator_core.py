from operations.basic_operations import BasicOperations
from operations.advanced_operations import AdvancedOperations

class CalculatorCore:
    """Core calculator functionality that coordinates operations"""

    def __init__(self):
        self.basic_ops = BasicOperations()
        self.advanced_ops = AdvancedOperations()
        self.history = []

    def perform_operation(self, choice: int, num1: float = None, num2: float = None):
        """Perform the selected operation"""
        operations = {
            1: ("Addition", lambda:self.basic_ops.add(num1, num2)),
            2: ("Subtraction", lambda:self.basic_ops.subtract(num1, num2)),
            3: ("Multiplication", lambda: self.basic_ops.multiply(num1, num2)),
            4: ("Division", lambda: self.basic_ops.divide(num1, num2)),
            5: ("Power", lambda: self.advanced_ops.power(num1, num2)),
            6: ("Square Root", lambda: self.advanced_ops.square_root(num1)),
            7: ("Factorial", lambda: self.advanced_ops.factorial(int(num1))),
            8: ("Percentage", lambda: self.advanced_ops.percentage(num1, num2))

        }

        if choice in operations:
            operation_name, operation_func = operations[choice]
            try:
                result = operation_func()
                self.history.append({
                    'operation': operation_name,
                    'operands': (num1, num2) if num2 is None else (num1,),
                    'result': result
                })

                return result, operation_name
            except Exception as e:
                raise e

    def get_history(self):
        """Return calculation history"""
        return self.history

    def clear_history(self):
        """Clear calculation history"""

        self.history = []