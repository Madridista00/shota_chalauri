"""1. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

    2. Car კლასს დაუმატეთ თითეული ატრიბუტისთვის set და get ფუნქციები მათი ცვლილებებისთვის.

    3. დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის ინტეგერი და ასე შემდეგ."""


class Car:

    def __new__(cls, *args, **kwargs):
        print("Object created")

        isinstance = super().__new__(cls)

        return isinstance

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year{self.year}"

    # getter
    @property
    def brand(self):
        return self._brand


    @property
    def model(self):
        return self._model
    

    @property
    def year(self):
        return self._year

    # setter
    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and value.isalpha():
            self._brand = value
        else:
            raise ValueError("Allowed only letters")


    @model.setter
    def model(self, value):
        if isinstance(value, str) and value.isascii():
            self._model = value
        else:
            raise ValueError("Allowed only letters or digits")
        
    
    @year.setter
    def year(self, value):
        if isinstance(value, int) and value > 0:
            self._year = value
        else:
            raise ValueError("Not integer, negative value and zero not allowed.")


#========================================
car_1 = Car("Mazda", "Verisa", 2005)
print(f"{car_1.car_info()}\n")

print(car_1.brand)
car_1.brand = "Toyota"
print(car_1.brand, "\n")

print(f"{car_1.car_info()}\n")

print(car_1.model)
car_1.model = "Camry"
print(car_1.model, "\n")

print(f"{car_1.car_info()}\n")

print(car_1.year)
car_1.year = 2024
print(car_1.year, "\n")

print(f"{car_1.car_info()}\n")
