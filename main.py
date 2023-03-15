import logging

from forecast_day_model import Base, ForecastDay
from question_6 import Forecaster
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")

if __name__ == "__main__":
    try:
        engine = create_engine(
            "postgresql://postgres:1234@localhost:5432/test_db_pg", echo=False
        )
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            result = Forecaster().get_forecast_data(True, hour=4, city="lahore", days=3)
            for i in result.get("forecastday"):
                day = ForecastDay(
                    daily_chance_of_rain=i.get("daily_chance_of_rain"),
                    daily_chance_of_snow=i.get("daily_chance_of_snow"),
                    condition=i.get("condition"),
                    temp_f=i.get("temp_f"),
                    pressure_in=i.get("pressure_in"),
                    humidity=i.get("humidity"),
                    cloud=i.get("cloud"),
                    feelslike_f=i.get("feelslike_f"),
                    dewpoint_f=i.get("dewpoint_f"),
                    vis_km=i.get("vis_km"),
                    gust_mph=i.get("gust_mph"),
                    air_quality=i.get("air_quality"),
                )
                session.add(day)
            session.commit()
    except Exception as e:
        logging.exception("Exception occured")
