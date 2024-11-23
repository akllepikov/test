class Shape:
    name:str = None
    def square(self) -> float:
        raise NotImplementedError()
    
    def __str__(self) -> str:
        return f"{self.name}(square={self.square()})"


R = 2
circle = Shape()
circle.name = "Circle"
circle.square=R*R


shapes: list = [
    Shape()
]

for s in shapes:
    print(s)
