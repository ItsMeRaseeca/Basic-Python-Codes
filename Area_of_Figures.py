print("Enter the choice of figure to calculate the area: ")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    pi = 3.14
    radius = float(input("Enter the radius of circle: "))
    if radius > 0:
        area = pi * radius ** 2
        print("The area of circle is " + str(area))
    else:
        print("Radius cannot be 0 or negative. It must be positive")

elif choice == 2:
    length = float(input("Enter the length of rectangle: "))
    breadth = float(input("Enter the breadth of rectangle: "))
    if length>0 and breadth>0:
        area = length * breadth
        print("The area of rectangle is: " + str(area))
    else:
        print("Length and breadth both must be positive and greater than 0")

elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    if base>0 and height>0:
        area = 1/2 * base * height
        print("The area of triangle is: " + str(area))
    else:
        print("Both Base and height of triangle should be greater than 0.")

else:
    print("Invalid choice!")
