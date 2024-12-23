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
        print ("The Sum is " + str(int(num1) + int(num2)))
    elif opertaion == "2":
        print("The Subtract is " + str(int(num1) - int(num2)))
    elif opertaion == "3":
        print("The multiply is " + str(int(num1) * int(num2)))
    elif opertaion == "4":
        print("The divide is " + str(int(num1) / int(num2)))
else:
    print("Please select valid entry")
