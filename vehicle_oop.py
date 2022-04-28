# class Vehicle:
#     def __init__(self):
#         print('Vehicle created')
#     def startIgnition(self):
#         pass  # Ignition starting code goes here.
#     def changeTire(self):
#         pass  # Change Tire code goes here.
#
# class Car(Vehicle):
#     def __init__(self):
#         print('Car created.')
#
# class Motorcycle(Vehicle):
#     def __init__(self):
#         print('Motorcycle created.')
#
# class LunarRover(Vehicle):
#     def __init__(self):
#         print('LunarRover created.')

class CombustionEngine:
    def __init__(self):
        print('Combustion engine created.')
    def changeSparkplug(self):
        pass  # Spark plug changing code goes here.

class ElectricEngine:
    def __init__(self):
        print('Electric Engine created.')

class Vehicle:
    def __init__(self):
        print('Vehicle created.')
        self.engine = CombustionEngine()  # Use this engine by deafult.

class LunarRover(Vehicle):
    changeSparkPlug = None
    def __init__(self):
        print('LunarRover created.')
        self.engine = ElectricEngine()