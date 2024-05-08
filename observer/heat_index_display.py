from weather_data import WeatherData
from observer import Observer
from display_element import DisplayElement


class HeatIndexDisplay(Observer, DisplayElement):
    heat_index: float = 0.0
    weather_data: WeatherData = WeatherData()

    def __init__(self, weather_data: WeatherData):
        super().__init__()
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.heat_index = self.compute_heat_index(temp, humidity)
        self.display()

    def compute_heat_index(self, t: float, rh: float):
        index: float = ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
                         (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) + (0.000345372 * (t * t * rh)) -
                         (0.000814971 * (t * rh * rh)) + (0.0000102102 * (t * t * rh * rh)) -
                         (0.000038646 * (t * t * t)) + (0.0000291583 * (rh * rh * rh)) +
                         (0.00000142721 * (t * t * t * rh)) + (0.000000197483 * (t * rh * rh * rh)) -
                         (0.0000000218429 * (t * t * t * rh * rh)) + 0.000000000843296 * (t * t * rh * rh * rh)) -
                        (0.0000000000481975 * (t * t * t * rh * rh * rh)))
        return index

    def display(self):
        print(f"Heat index is: {self.heat_index}")
