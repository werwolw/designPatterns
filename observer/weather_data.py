from observer import Observer
from subject import Subject


class WeatherData(Subject):
    observers: list
    temperature: float
    humidity: float
    pressure: float

    def __init__(self):
        self.observers = []

    def register_observer(self, obs: Observer):
        self.observers.append(obs)

    def remove_observer(self, obs: Observer):
        self.observers.remove(obs)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure
