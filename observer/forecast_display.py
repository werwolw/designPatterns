from display_element import DisplayElement
from observer import Observer
from weather_data import WeatherData


class ForecastDisplay(Observer, DisplayElement):
    current_pressure: float = 240.0
    last_pressure: float = 0.0
    weather_data: WeatherData

    def __init__(self, weather_data: WeatherData):
        super().__init__()
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self.last_pressure = self.current_pressure
        self.current_pressure = self.weather_data.get_pressure()

        self.display()

    def display(self):
        print("Forecast: ")
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        elif self.current_pressure < self.last_pressure:
            print("Watch out for cooler, rainy weather")
