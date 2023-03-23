import logging
from datetime import date

from models import Base, Condition, Day, Location, Temprature, Wind
from sqlalchemy import and_, create_engine, desc, func
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

    def get_forecasted_data(self, city: str) -> list[Day]:
        """
        This function takes in the city and returns the forecasted temprature
        of all the available after the current day.
        """
        with Session(self.__engine) as session:
            current_date = date.today()
            days = (
                session.query(Day)
                .join(Location)
                .join(Temprature)
                .filter(
                    and_(
                        Day.day_date >= current_date,
                        func.lower(Location.name) == city.lower(),
                        Day.is_current == False,
                    )
                )
                .all()
            )
            return days

    def get_temperature(self, days: list[Day]) -> Temprature:
        """
        This function takes a list of days and return the max temprature among the list of
        days
        """
        list_of_ids = list()
        [list_of_ids.append(day.id) for day in days]
        with Session(self.__engine) as session:
            """
            The below query is same as
            select * from temprature where id == (select max(id) from temprature where id in (list_of_ids))
            """
            temp = (
                session.query(Temprature)
                .filter(
                    Temprature.id
                    == (
                        session.query(func.max(Temprature.id))
                        .filter(Temprature.day_id.in_(list_of_ids))
                        .first()[
                            0
                        ]  # since sub query return a tuple so its 0th index has the highest value
                    )
                )
                .first()
            )
        return temp

    def get_second_humid_city(self):
        with Session(self.__engine) as session:
            current_date = date.today()
            """
            The below query groups the data based on city then find the avg humidty of each group 
            and return the sorted list in reverse order.
            sample output:
            [   
                (Decimal('69.3000000000000000'), 'Karachi'), 
                (Decimal('61.8333333333333333'), 'Lahore'), 
                (Decimal('60.1666666666666667'), 'Islamabad')
            ]
            """
            days = (
                session.query(func.avg(Wind.humidity), Location.name)
                .select_from(Wind)
                .join(Day)
                .join(Location)
                .filter(
                    and_(
                        Day.day_date >= current_date,
                        Day.is_current == False,
                    )
                )
                .group_by(Location.name)
                .order_by(func.avg(Wind.humidity).desc())
                .all()
            )
            return days
