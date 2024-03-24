import pytest
from vehicle import Vehicle, ElectricVehicle


class TestVehicle:
    @classmethod
    def setup_class(CLS):
        print("Setting up class\n")


    @classmethod
    def teardown_class(CLS):
        print("tearing down class\n")


    def setup_method(self, method):
        print(f"Setting up {method}")

        self.vehicle = Vehicle("Lamborghini", "Aventador", 2024)

    def teardown_method(self, method):
          print(f"Tiering down {method}")

    def test_fuel_up(self):
        print("test_fuel_up")

        assert self.vehicle.fuel_up == "Gas tank is now full or can move."

    def test_drive(self):
        print("test_drive")

        assert self.vehicle.drive == "The Aventador is now driving."


class TestElectricVehicle:
    def teardown_class(CLS):
        print("tearing down class\n")


    def setup_method(self, method):
        print(f"Setting up {method}")

        self.el_vehicle = ElectricVehicle("Tesla", "Model S", 2023)

    def teardown_method(self, method):
          print(f"Tiering down {method}")


    def test_charge(self):
        print("test_charge")

        assert self.el_vehicle.charge == "The vehicle is now charged."

    def test_fuel_up_electric_vehicle(self):
        print("test_fuel_up_electric_vehicle")

        assert self.el_vehicle.fuel_up == "This vehicle has no fuel tank!"