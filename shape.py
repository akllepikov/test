import math


class Shape:
    name:str = None
    def square(self) -> float:
        raise NotImplementedError()
    
    def __str__(self) -> str:
        return f"{self.name}(square={self.square()})"


class Circle(Shape):
    name: str = "Circle"
    def __init__(self, R):
        self.R = R
    def square(self) -> float:
        return  self.R*self.R* math.pi 

class Triangle(Shape):
    name: str= "Triangle"
    def __init__(self, B, H):
        self.B = B
        self.H = H
    def square(self) ->float:
        return self.B*self.H/2

shapes: list = [
     Circle(2) , Triangle(1,2)
    ]

for s in shapes:
    print(s)
