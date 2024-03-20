# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
# class ConsoleDisplay:
#     def show(self, data):
#         pass

from abc import ABC, abstractmethod

class WeatherStation:
    def report(self, display):
        display.show("Weather Data")


class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass


class ConsoleDisplay(Display):
    def show(self, data):
        print(data)


class WeatherStation:
    def report(self, display):
        display.show("Weather data")


#==============
console_display = ConsoleDisplay()
weather_station = WeatherStation()
weather_station.report(console_display)