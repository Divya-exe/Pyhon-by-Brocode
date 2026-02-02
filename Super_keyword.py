class Shapes:
    def __init__(self, color,is_filled):
        self.color=color
        self.is_filled= is_filled
        
    def describe(self):
        print(f"It is {self.color} & {'filled' if self.is_filled else 'not filled'}")
class Circle(Shapes):
    def __init__(self, color ,is_filled,radius):
        super().__init__(color, is_filled)
        self.radius= radius
        
    def describe(self):
        print(f"it is a circle with an area of {3.14 * self.radius}cm^2")
        super().describe()
        
class Square(Shapes):
    def __init__(self, color ,is_filled,width):
        super().__init__(color, is_filled)
        self.width= width
        
    def describe(self):
        print(f"it is a square with an area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shapes):
    def __init__(self, color ,is_filled,width,height):
        super().__init__(color, is_filled)
        self.width= width
        self.height= height
        
    def describe(self):
        print(f"it is a Triangle with an area of {self.width * self.height /2 }cm^2")
        super().describe()
    

shapes=Shapes("red",True)
circle=Circle("blue",True, 4)
square=Square("yellow",False, 6)
triangle=Triangle("black",True, 2 , 3)
shapes.describe()
print()
circle.describe()
print()
square.describe()
print()
triangle.describe()

        