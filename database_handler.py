import logging

from models import Base, Condition, Day, Location, Temprature, Wind
from sqlalchemy import and_, create_engine, desc
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")


class db_handler:
    def __init__(self) -> None:
        self.__engine = create_engine(
            "postgresql://postgres:1234@localhost:5432/test_db_pg", echo=False
        )
        Base.metadata.create_all(self.__engine)

    def insertData(
        self,
        day: Day,
        location: Location,
        wind: Wind,
        temprature: Temprature,
        condition: Condition,
    ) -> None:
        """
        Takes the modal objects and links the day object with the all other objects for foreign key relations
        and inserts them into database, only if record is not already present.
        """
        try:
            with Session(self.__engine) as session:
                exsisted_day = (
                    session.query(Day)
                    .join(Location)
                    .filter(
                        and_(
                            Day.day_date == day.day_date,
                            Location.name == location.name,
                            Day.is_current == day.is_current,
                        )
                    )
                    .first()
                )
                if exsisted_day == None:
                    logging.info("Inserting forcasted data into DB")
                    session.add(day)
                    last_day = session.query(Day).order_by(desc(Day.id)).first()
                    location.day = last_day
                    wind.day = last_day
                    temprature.day = last_day
                    condition.day = last_day
                    session.add(location)
                    session.add(wind)
                    session.add(temprature)
                    session.add(condition)
                    session.commit()
                    logging.info("Forecasted data inserted!")
                else:
                    logging.info("Record already present. Nothing Changed")
        except Exception as e:
            logging.exception("Exception occured")
