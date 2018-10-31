class Circle:

    def __init__(self, r):
        # Get "r" parameter and set as class parameter.
        self.radius = r

    def area(self):
        # return radius ** 2 * 3.14
        return self.radius ** 2 * 3.14

    def perimeter(self):
        # return radius * 2 * 3.14
        return 2 * self.radius * 3.14


NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
