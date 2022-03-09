class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = "White"


    def car_description(self):
        long_name = f"Vehicle name: {self.name} Vehicle speed: {self.max_speed} Vehicle mileage: {self.mileage}"
        return long_name

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def update_color(self, shade):
        self.color = shade

    def vehicle_color(self):
        description = f"{self.name} color is {self.color}"
        return description

my_car = Vehicle("Bug", "60mph", "120_000")
print(my_car.car_description())
my_car.update_color("blue")
print(my_car.vehicle_color())


class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__( name, max_speed, mileage)


my_bus = Bus("VW", "25mph", "35")
print(my_bus.car_description())
print(my_bus.seating_capacity(50))

class Car(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__( name, max_speed, mileage)

    def describe_color(self):
        tone = f"{self.name} color is {self.color}"
        return tone




my_car = Car("Audi Q5", 240, 18)
print(my_car.car_description())
print(my_car.describe_color())



