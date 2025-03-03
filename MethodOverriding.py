import math

class Shape:
    def area():
        print("This method is to be overwritten by child classes")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return length*width

class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return 0.5*length*height


while True:
    print("Area Calculator: ")
    print("1. Circle \n 2. Rectangle \n 3. Triangle \n 4. Exit")

    choice = int(input("Enter the choice of shape which you want to calculate area for: "))

    if choice == 1:
        radius = float(input("Enter radius: "))
        shape = Circle(radius)
        
    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        shape = Rectangle(length, width)

    elif choice == 3:
        length = float(input("Enter length: "))
        height = float(input("Enter height: "))
        shape = Triangle(length, height)

    elif choice == 4:
        print("Exiting")
        break
    
    else:
        print("Invalid choice!!!!!!!")

    print(f"The area of shape is: {shape.area():.2f}")
