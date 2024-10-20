

class Car:
    name: str
    _speed: int
    direction: str

    def __init__(self, name: str, speed: int, direction: str):
        self.name = name
        self._speed = speed
        self.direction = direction

    def __call__(self):
        print(f"{self.name} is going at the speed of {self._speed} in the {self.direction} direction currently.")

    def accelerate(self, speed: int) -> None:
        self._speed += speed

    def decelerate(self, speed: int) -> None:
        self._speed -= speed



bmw = Car("bmw",  100, "straight")
yugo = Car("yugo", 50, "left")
toyota = Car("toyota", 70, "straight")

print(bmw)


bmw()
bmw.accelerate(50)
bmw()
bmw.decelerate(20)
bmw()
bmw._speed = 100
bmw()