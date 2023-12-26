# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     color = "white"
#
#     def seating_capacity(self, capacity):
#         return f"The capacity {self.name} is {capacity}"
#
#     def total_fare(self):
#         return self.seating_capacity() * 100
#
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)
#
#     def total_fare(self):
#         super().total_fare() + .1 * float(super().total_fare())
#
#
# class Car(Vehicle):
#     def seating_capacity(self, capacity=5):
#         return super().seating_capacity(capacity)
#
#
# School_Bus = Bus("Volvo bus", 340, 48)
# print(School_Bus.total_fare())
#
# School_car = Car("audi", 200, 39)
# print(School_car.color, School_car.seating_capacity())
#
# modelX = Vehicle("tucson", 250, 48)
# print(modelX.mileage)


class Vehicle:
    pass


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def fare(self):
        bus_fare = super().fare() + 0.1 * super().fare()
        return bus_fare


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print("is instance:", isinstance(School_bus, Bus))