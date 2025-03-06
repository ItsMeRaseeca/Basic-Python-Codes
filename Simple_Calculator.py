
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError
        return x / y
    except ZeroDivisionError:
        print("Cannot divide a number by zero!")
        return None

def calculator():
    try:
        while True:
            print("Select operation:")
            print("1. Add \n2. Subtract\n3. Multiply \n4. Divide \n5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 5:
                print("Exiting calculator.")
                break  

            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))

            if choice == 1:
                print(add(num1, num2))
            elif choice == 2:
                print(subtract(num1, num2))
            elif choice == 3:
                print(multiply(num1, num2))
            elif choice == 4:
                result = divide(num1, num2)
                if result is not None:
                    print(result)
            else:
                print("Invalid choice! Please enter a valid choice")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculator()
