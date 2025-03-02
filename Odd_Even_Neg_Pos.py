num = float(input("Enter a number: "))

if num > 0:
    result = "positive"
elif num < 0:
    result = "negative"
else:
    result = "neither positive nor negative (zero)"

if num % 2 == 0:
    result += " and even."
else:
    result += " and odd."

print("The number is " + result)
