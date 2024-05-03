from observer.display_element import DisplayElement
from observer.observer import Observer
from observer.subject import Subject


class CurrentConditionsDisplay(Observer, DisplayElement):
    temperature: float
    humidity: float
    pressure: float
    weather_data: Subject

    def __init__(self, weather_data):
        super().__init__()
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} F degrees and {self.humidity} % humidity "
              f"and {self.pressure} Pa pressure")
