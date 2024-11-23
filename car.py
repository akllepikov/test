class Vehicle:
    color: str

    def __init__(self, color: str) -> None:
        self.color = color

class MotorVehicle:
    power: float = None

    def __init__(self, power: float) -> None:
        self.power = power

class TransportVehicle:
    seats: int = None

    def __init__(self, seats: int) -> None:
        self.seats = seats

class Car(Vehicle, MotorVehicle, TransportVehicle):
    def __init__(self, color: str, power: float, seats: int) -> None:
        Vehicle.__init__(self, color)
        MotorVehicle.__init__(self, power)
        TransportVehicle.__init__(self, seats)

    def __str__(self):
        return f"Car(color={self.color}, power={self.power}, seats={self.seats})"

car1 = Car("red", 180, 5)
car2 = Car("red", 280, 5)
print(str(car1), car2)
