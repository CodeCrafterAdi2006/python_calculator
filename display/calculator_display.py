class CalculatorDisplay:
    """Handles display and user interface"""

    @staticmethod
    def show_menu():
        """Display the calculator menu"""
        print("\n" + "="*40)
        print("          CALCULATOR MENU")
        print("="*40)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Factorial (!)")
        print("8. Percentage (%)")
        print("9. Exit")
        print("="*40)

    @staticmethod
    def get_operation_choice() -> int:
        """Get operation choice from user """
        try:
            choice = int(input("Enter your choice (1-9): "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Please enter a number between 1 and 9")
                return CalculatorDisplay.get_operation_choice()
        except ValueError:
            print("Please enter a Valid number")
            return CalculatorDisplay.get_operation_choice()

    @staticmethod
    def get_number(prompt: str) -> float:
        """Get a number from user with validation"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number")

    @staticmethod
    def show_result(operation: str, result: float):
        """Display the result of an operation"""
        print(f"\n{operation} Result: {result}")


    @staticmethod
    def show_error(message: str):
        """Display error messages"""
        print(f"Error: {message}")