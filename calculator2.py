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


def main():
    calc = Calculator2()

    while True:
        print("\nPlease Select the operation you want")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. EXIT")

        opertaion = input("Enter your choice: ")

        if opertaion == "5":
            print("Exiting the program. Goodbye!")
            break

        if opertaion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if opertaion == "1":
                    print(f"The result is: {calc.add(num1, num2)}")
                elif opertaion == "2":
                    print(f"The result is: {calc.subtract(num1, num2)}")
                elif opertaion == "3":
                    print(f"The result is: {calc.multiply(num1, num2)}")
                elif opertaion == "4":
                    print(f"The result is: {calc.divide(num1, num2)}")

            except ValueError:
                print("Error: Please enter valid numeric values for the numbers.")

            # Handles unexpected errors
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Please select a valid operation (1, 2, 3, 4, or 5).")


if __name__ == "__main__":
    main()
