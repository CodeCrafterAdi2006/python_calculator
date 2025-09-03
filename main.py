from tkinter.messagebox import showerror

from core.calculator_core import CalculatorCore
from display.calculator_display import CalculatorDisplay

def main():
    """Main function to run the calculator"""

    calculator = CalculatorCore()
    display = CalculatorDisplay()

    print("Welcome to the OOP Calculator!")

    while True:
        display.show_menu()
        choice = display.get_operation_choice()

        if choice == 9:
            print("Thank you for using the calculator!")
            break

        try:
            if choice in [1, 2, 3, 4, 5, 8]: #Operations requiring two numbers
                num1 = display.get_number("Enter first number: ")
                num2 = display.get_number("Enter second number: ")
                result, operation_name = calculator.perform_operation(choice, num1, num2)
                display.show_result(operation_name, result)

            elif choice in [6,7]: #operations requiring one number
                num1 = display.get_number("Enter number: ")
                result, operation_name = calculator.perform_operation(choice, num1)
                display.show_result(operation_name, result)
        except Exception as e:
            display.show_error(str(e))

if __name__ == "__main__":
    main()