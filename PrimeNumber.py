#Write a program to calculate prime number using function-

#LOFI GIRL LOGIC- A number n is only divisible by numbers ≤ n, and if it has a
#factor greater than √n, its corresponding pair will already be checked below √n.

def is_Prime(num):
    if num<2:
        return False

    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_Prime(number):
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is not a Prime Number.")
