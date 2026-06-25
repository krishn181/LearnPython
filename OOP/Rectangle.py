class Rectangle:
    def __init__ (self, length : float, breadth : float):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return (self.length * self.breadth)

    def perimeter(self):
        return 2*(self.length + self.breadth)

r = Rectangle(20,21)
print(r.area())
print(r.perimeter())