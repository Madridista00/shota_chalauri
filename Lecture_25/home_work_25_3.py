# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle
# class Vehicle:
#     def fuel_capacity(self):
#         return "100 liters"

# class ElectricCar(Vehicle):
#     def fuel_capacity(self):
#         return "Battery capacity is 100 kWh"

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def fuel_capacity(self):
        pass


class Car(Vehicle):
    def fuel_capacity(self):
        return "100 liters"


class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"


# ==========================
car1 = Car()
print(car1.fuel_capacity())

electriccar1 = ElectricCar()
print(electriccar1.fuel_capacity())
