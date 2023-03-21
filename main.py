import logging

from database_handler import db_handler
from models import Condition, Day, Location, Temprature, Wind
from question_5 import WeatherForecaster
from question_6 import Forecaster

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")


def dump_forecasted_data(city: str, interval: int = 0) -> None:
    result = Forecaster().get_forecast_data(True, hour=4, city=city, days=interval)
    for i in result.get("forecastday"):
        location = Location(
            name=result.get("city"),
            latitude=result.get("latitude"),
            longitude=result.get("longitude"),
        )
        day = Day(is_current=False, day_date=i.get("date"))
        wind = Wind(
            vis_km=i.get("vis_km"),
            gust_mph=i.get("gust_mph"),
            humidity=i.get("humidity"),
        )
        temp = Temprature(temp_f=i.get("temp_f"), feelslike_f=i.get("feelslike_f"))
        condition = Condition(
            daily_chance_of_rain=i.get("daily_chance_of_rain"),
            daily_chance_of_snow=i.get("daily_chance_of_snow"),
            condition=i.get("condition"),
            pressure_in=i.get("pressure_in"),
            cloud=i.get("cloud"),
            dewpoint_f=i.get("dewpoint_f"),
            air_quality=i.get("air_quality"),
        )
        handle = db_handler()
        handle.insertData(day, location, wind, temp, condition)


def dump_current_data(city: str) -> None:
    result = WeatherForecaster().get_current_weather(True, city=city)
    location = Location(
        name=result.get("city"),
        latitude=result.get("latitude"),
        longitude=result.get("longitude"),
    )
    day = Day(is_current=True, day_date=result.get("date_time"))
    wind = Wind(
        vis_km=result.get("vis_km"),
        gust_mph=result.get("gust_mph"),
        humidity=result.get("humidity"),
    )
    temp = Temprature(
        temp_f=result.get("temp_f"), feelslike_f=result.get("feelslike_f")
    )
    condition = Condition(
        daily_chance_of_rain=None,
        daily_chance_of_snow=None,
        condition=result.get("condition"),
        pressure_in=result.get("pressure_in"),
        cloud=result.get("cloud"),
        dewpoint_f=None,
        air_quality=result.get("air_quality"),
    )
    handle = db_handler()
    handle.insertData(day, location, wind, temp, condition)


if __name__ == "__main__":
    try:
        dump_forecasted_data(city="Lahore", interval=4)
        dump_current_data("lahore")
    except Exception as e:
        logging.exception("Exception occured")
