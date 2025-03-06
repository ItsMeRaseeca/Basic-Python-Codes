# [::1] is just a shortcut method to reverse a number, nothing else.

num = int(input("Enter a number: "))

reverse_num = int(str(num)[::-1])

if reverse_num == num:
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")
