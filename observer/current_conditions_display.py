from display_element import DisplayElement
from observer import Observer
from weather_data import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    temperature: float
    humidity: float
    pressure: float
    weather_data: WeatherData

    def __init__(self, weather_data: WeatherData):
        super().__init__()
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} F degrees and {self.humidity} % humidity ")
