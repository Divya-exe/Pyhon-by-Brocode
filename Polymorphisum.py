from abc import ABC,abstractmethod
class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shapes):
    def __init__(self, radius):
        self.radius=radius
        
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shapes):
    def __init__(self, width):
        self.width=width
        
    def area(self):
        return self.width * self.width

class Triangle(Shapes):
    def __init__(self, base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base * self.height * 0.5
        
# cir=Circle(2)
# print(cir.area())
# print()
# sqr=Square(2)
# print(sqr.area())
# print()
# tri=Triangle(2,2)
# print(tri.area())

shapes=[Circle(2),Square(2),Triangle(2,2)]
for shape in shapes:
    print(f"{shape.area()}cm^2")
