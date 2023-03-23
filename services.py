import json

from database_handler import db_handler
from models import Condition, Day, Location, Temprature, Wind
from question_5 import WeatherForecaster
from question_6 import Forecaster


def dump_forecasted_data(city: str, interval: int = 0) -> None:
    """
    This function fetchs the forecast API and dumps it into database.
    Only dumps into the db if record is not already present.\n
    Required parameters
    -------------------
    city
        Name of the city to fetch data for.
    interval
        Number of days to fetch data for.
    """
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
    """
    This function fetchs the current API and dumps it into database.
    Only dumps into the db if record is not already present.\n
    Required parameters
    -------------------
    city
        Name of the city to fetch data for.
    """
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


def get_highest_temp_values(city: str) -> str:
    """
    TASK 4
    ------
    This function takes a city as input and outputs the day with the
    highest daily temperature difference in the next 7 days.
    If the required data is not in the database, an api call is made to add that data.
    """
    # This dump function add the 7 day forecasted data into the DB, Only if data is not already present.
    # This makes sure that the required data is always in the DB.
    dump_forecasted_data(city, 7)
    db = db_handler()
    days = db.get_forecasted_data(city)
    pass


def get_hottest_day(city: str, interval: int) -> str:
    """
    TASK 1
    ------
    This function takes the city and range of days and calculates the hottest forecasted day in that range.
    """
    dump_forecasted_data(city, interval)
    db = db_handler()
    days = db.get_forecasted_data(city)[:interval:]
    max_temp = db.get_temperature(days)
    # creating the required result.
    for i in days:
        if i.id == max_temp.day_id:
            return json.dumps(
                {
                    "day": i.day_date.strftime("%m/%d/%Y, %H:%M:%S"),
                    "temp_f": max_temp.temp_f,
                }
            )
    return json.dump({"error": "Something went wrong :("})
