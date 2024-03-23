import unittest
from vehicle import Vehicle, ElectricVehicle


class TestVehicle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup Class for TestVehicle")

    @classmethod
    def tearDownClass(cls):
        print("teardown Class for TestVehicle")

    def setUp(self):
        print("setUp for TestVehicle")

        self.vehicle = Vehicle("Lamborghini", "Aventador", 2024)

    def tearDown(self):
        print("tearDown for TestVehicle\n")

    def test_fuel_up(self):
        print("test_fuel_up")

        self.assertEqual(self.vehicle.fuel_up, "Gas tank is now full or can move.")

    def test_drive(self):
        print("test_drive")

        self.assertEqual(self.vehicle.drive, "The Aventador is now driving.")


class TestElectricVehicle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup Class for TestElectricVehicle")

    @classmethod
    def tearDownClass(cls):
        print("teardown Class for TestElectricVehicle")

    def setUp(self):
        print("setUp for TestElectricVehicle")

        self.el_vehicle = ElectricVehicle("Tesla", "Model S", 2023)

    def tearDown(self):
        print("tearDown for TestElectricVehicle\n")

    def test_charge(self):
        print("test_charge")

        self.assertEqual(self.el_vehicle.charge, "The vehicle is now charged.")

    def test_fuel_up_electric_vehicle(self):
        print("test_fuel_up_electric_vehicle")

        self.assertEqual(self.el_vehicle.fuel_up, "This vehicle has no fuel tank!")


# ==========================
if __name__ == "__main__":
    unittest.main()