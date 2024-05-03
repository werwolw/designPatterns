from observer.observer import Observer
from observer.subject import Subject


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
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
