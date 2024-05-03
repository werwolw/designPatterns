from observer.current_conditions_display import CurrentConditionsDisplay
from observer.forecast_display import ForecastDisplay
from observer.statistics_display import StatisticsDisplay
from observer.weather_data import WeatherData

if __name__ == "__main__":
    weather_data = WeatherData()

    current_condition_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(10, 80, 450)
    weather_data.set_measurements(11, 81, 451)
    weather_data.set_measurements(12, 82, 452)

