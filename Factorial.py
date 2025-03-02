#WAP to calculate factorial using function

#For inputs 0 and 1, the for loop doesnt run, making the factorial of 0 -> 1 and 1 -> 1


def factorial(num):
    if num<0:
        return "Not defined for negative numbers."
    
    result = 1

    for i in range(2, num+1):
        result *= i

    return result

number = int(input("Enter a number: "))

print(f"The factorial of {number} is {factorial(number)}.")

