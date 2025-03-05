def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

try:
    temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    converted_celsius = fahrenheit_to_celsius(temp_in_fahrenheit)
    print(f"{temp_in_fahrenheit:.2f}°F is equivalent to {converted_celsius:.2f}°C")
except ValueError:
    print("Invalid Input! Please enter a valid input")

try:
    temp_in_celsius = float(input("\nEnter temperature in Celsius: "))
    converted_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
    print(f"{temp_in_celsius:.2f}°C is equivalent to {converted_fahrenheit:.2f}°F")
except ValueError:
    print("Invalid Input! Please enter a valid input")
