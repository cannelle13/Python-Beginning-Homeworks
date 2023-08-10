class Car:
    def __init__(self, brand, model, year, speed) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self) -> str:
        return f"My car is {self.brand} {self.model} of {self.year} and max speed {self.speed} km/h."

    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed -= 5
        return self.speed


my_car = Car("Suzuki", "Jimny", 2023, 145)

print(my_car)
my_car.accelerate()
print(my_car)
my_car.brake()
print(my_car)
