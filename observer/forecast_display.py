from display_element import DisplayElement
from observer import Observer
from subject import Subject


class ForecastDisplay(Observer, DisplayElement):
    current_pressure: float = 240.0
    last_pressure: float = 0.0
    weather_data: Subject

    def __init__(self, weather_data):
        super().__init__()
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure

        self.display()

    def display(self):
        print("Forecast: ")
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        elif self.current_pressure < self.last_pressure:
            print("Watch out for cooler, rainy weather")
