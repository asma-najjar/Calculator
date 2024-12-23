class Calculator2:
    def add(self, a,b):
        return a+b

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

    print("Please Select the operation you want")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")

    opertaion = input("enter your choice: ")

    if opertaion in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first num: "))
        num2 = float(input("Enter the Second num: "))

        if opertaion == "1":
            print (f"The result is: {calc.add(num1, num2)}")
        elif opertaion == "2":
            print(f"The result is: {calc.subtract(num1, num2)}")
        elif opertaion == "3":
            print(f"The result is: {calc.multiply(num1, num2)}")
        elif opertaion == "4":
            print(f"The result is: {calc.divide(num1, num2)}")
    else:
        print("Please select valid entry")

if __name__ == "__main__":
    main()