class Calculator2:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is undefined"
        return a / b

    def evaluate_parentheses(self, tokens):
        stack = []
        for token in tokens:
            if token == ")":
                sub_expr = []
                while stack and stack[-1] != "(":
                    sub_expr.append(stack.pop())
                if not stack:
                    return "Error: Mismatched parentheses"
                stack.pop()  # Remove the "("
                sub_expr.reverse()  # Reverse to correct order
                sub_result = self.calculate_multiple_operations(" ".join(sub_expr))
                stack.append(str(sub_result))
            else:
                stack.append(token)
        return stack

    def calculate_multiple_operations(self, expression):
        try:
            # Tokenize the input
            tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
            if not tokens:
                return "Error: Empty expression"

            # Handle parentheses
            tokens = self.evaluate_parentheses(tokens)

            # Evaluate the flat expression (no parentheses at this point)
            if isinstance(tokens, str):  # If a single number is returned
                return float(tokens)

            result = float(tokens[0])
            for i in range(1, len(tokens), 2):
                operator = tokens[i]
                operand = float(tokens[i + 1])

                if operator == "+":
                    result = self.add(result, operand)
                elif operator == "-":
                    result = self.subtract(result, operand)
                elif operator == "*":
                    result = self.multiply(result, operand)
                elif operator == "/":
                    if operand == 0:
                        return "Error: Division by zero is undefined"
                    result = self.divide(result, operand)
                else:
                    return f"Error: Unsupported operator '{operator}'"

            return result
        except ZeroDivisionError:
            return "Error: Division by zero is undefined"
        except ValueError:
            return "Error: Invalid number in expression"
        except Exception as e:
            return f"Error: {e}"


def main():
    calc = Calculator2()

    while True:
        print("\nPlease Select the operation you want:")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. EVALUATE ANY EXPRESSION")
        print("6. EXIT")

        operation = input("Enter your choice: ")

        if operation == "6":
            print("Exiting the program. Goodbye!")
            break

        if operation in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operation == "1":
                    print(f"The result is: {calc.add(num1, num2)}")
                elif operation == "2":
                    print(f"The result is: {calc.subtract(num1, num2)}")
                elif operation == "3":
                    print(f"The result is: {calc.multiply(num1, num2)}")
                elif operation == "4":
                    print(f"The result is: {calc.divide(num1, num2)}")

            except ValueError:
                print("Error: Please enter valid numeric values.")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif operation == "5":
            expression = input("Enter any mathematical expression you want to evaluate (e.g., 2 + 3 * (4 - 5)): ")
            result = calc.calculate_multiple_operations(expression)
            print(f"The result is: {result}")

        else:
            print("Please select a valid operation (1, 2, 3, 4, 5, or 6).")


if __name__ == "__main__":
    main()
