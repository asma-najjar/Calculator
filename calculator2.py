import operator
import re


class Calculator2:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': self.safe_divide
        }

    def safe_divide(self, a, b):
        if b == 0:
            raise ValueError("Error: Division by zero is undefined")
        return a / b

    @staticmethod
    def is_valid_parentheses(expression):
        stack = []
        matching_parentheses = {')': '(', '}': '{', ']': '['}

        for char in expression:
            if char in matching_parentheses:
                top = stack.pop() if stack else '#'
                if matching_parentheses[char] != top:
                    return False
            elif char in "({[":
                stack.append(char)

        return not stack

    def apply_operator(self, operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        result = self.operations[operator](left, right)
        values.append(result)

    def calculate_expression(self, expression):
        try:
            # Validate input expression
            if not expression.strip():
                raise ValueError("Expression cannot be empty.")

            operators = []
            values = []

            i = 0
            while i < len(expression):
                char = expression[i]

                if char.isdigit() or char == '.':
                    num = []
                    while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                        num.append(expression[i])
                        i += 1
                    values.append(float("".join(num)))
                    continue

                elif char in self.operations:
                    while (operators and operators[-1] in self.operations and
                           ((char in '+-' and operators[-1] in '*/') or
                            (char in '+-' and operators[-1] in '+-') or
                            (char in '*/' and operators[-1] in '*/'))):
                        self.apply_operator(operators, values)
                    operators.append(char)

                elif char == '(':
                    operators.append(char)

                elif char == ')':
                    while operators and operators[-1] != '(':
                        self.apply_operator(operators, values)
                    operators.pop()  # Remove '('

                i += 1

            while operators:
                self.apply_operator(operators, values)

            return values[0] if values else 0

        except Exception:
            raise ValueError("Please enter valid numbers.")

def main():
    calc = Calculator2()  # Create a calculator instance

    while True:
        print("\nPlease select the operation you want:")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. EVALUATE AN EXPRESSION")
        print("6. EXIT")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Exiting. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    print(f"Result: {calc.operations['+'](num1, num2)}")
                elif choice == "2":
                    print(f"Result: {calc.operations['-'](num1, num2)}")
                elif choice == "3":
                    print(f"Result: {calc.operations['*'](num1, num2)}")
                elif choice == "4":
                    try:
                        print(f"Result: {calc.operations['/'](num1, num2)}")
                    except ValueError as ve:
                        print(f"Error: {ve}")

            except ValueError:
                print("Error: Please enter valid numbers.")
            except Exception as e:
                print(f"Unexpected Error: {e}")

        elif choice == "5":  # Evaluate a complex expression
            expression = input("Enter any complex mathematical expression: ")

            if not calc.is_valid_parentheses(expression):
                print("Error: Parentheses are unmatched or incorrectly placed.")
                continue

            try:
                result = calc.calculate_expression(expression)
                print(f"Result: {result}")
            except ValueError as ve:
                print(f"Input Error: {ve}")
            except Exception as e:
                print(f"Error evaluating expression: {e}")

        else:
            print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
