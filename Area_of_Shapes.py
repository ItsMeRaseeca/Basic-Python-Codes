#WAP to calculate area of different shapes
import math

class ShapeAreas:
    def area_circle(self, radius):
        area = math.pi*radius**2
        print(f"The Area of Circle is {area:.2f}")

    def area_rectangle(self, length, width):
        area = length*width
        print(f"The Area of Rectangle is {area:.2f}")

    def area_triangle(self, length, height):
        area = 0.5*length*height
        print(f"The Area of Triangle is {area:.2f}")

c1 = ShapeAreas()
c1.area_circle(3)

r1 = ShapeAreas()
r1.area_rectangle(5, 3)

t1 =ShapeAreas()
t1.area_triangle(7, 4)

