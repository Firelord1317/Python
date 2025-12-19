import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Take radius from the user
r = float(input("Enter the radius of the circle: "))

# Create Circle object
c = Circle(r)

# Display results
print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perimeter())
