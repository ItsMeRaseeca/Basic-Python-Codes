print("Choose the arithmetic operation you want to perform:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")

choice = int(input("Enter your choice: "))

if choice == 1:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("The result of addition is: " + str(result))

elif choice == 2:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("The result of subtraction is: " + str(result))

elif choice == 3:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("The result of multiplication is: " + str(result))

else:
    print("Invalid choice!")
