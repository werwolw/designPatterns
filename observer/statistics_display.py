from display_element import DisplayElement
from observer import Observer
from subject import Subject


class StatisticsDisplay(Observer, DisplayElement):
    max_temp: float = 0.0
    min_temp: float = 0.0
    temp_sum: float = 0.0
    num_reading: int = 0
    weather_data: Subject

    def __init__(self, weather_data):
        super().__init__()
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temp_sum += temp
        self.num_reading += 1

        if temp > self.max_temp:
            self.max_temp = temp

        if temp < self.min_temp:
            self.min_temp = temp

        self.display()

    def display(self):
        print(f"Avg/Max/Min temperature = {self.temp_sum/self.num_reading}/"
              f"{self.max_temp}/{self.min_temp}")
