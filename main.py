import logging

from database_handler import db_handler
from models import Condition, Day, Location, Temprature, Wind
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
        handle.insertForecastedData(day, location, wind, temp, condition)


if __name__ == "__main__":
    try:
        dump_forecasted_data(city="Islamabad", interval=4)
    except Exception as e:
        logging.exception("Exception occured")
