# from sqlalchemy import Float, Integer, String
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# class Base(DeclarativeBase):
#     pass


# class ForecastDay(Base):
#     __tablename__ = "DailyForecasts"

# id: Mapped[int] = mapped_column(primary_key=True)
# daily_chance_of_rain: Mapped[int] = mapped_column(Integer())
# daily_chance_of_snow: Mapped[int] = mapped_column(Integer())
# condition: Mapped[str] = mapped_column(String(50))
# temp_f: Mapped[float] = mapped_column(Float())
# pressure_in: Mapped[float] = mapped_column(Float())
# humidity: Mapped[int] = mapped_column(Integer())
# cloud: Mapped[int] = mapped_column(Integer())
# feelslike_f: Mapped[float] = mapped_column(Float())
# dewpoint_f: Mapped[float] = mapped_column(Float())
# vis_km: Mapped[int] = mapped_column(Integer())
# gust_mph: Mapped[float] = mapped_column(Float())
# air_quality: Mapped[str] = mapped_column(String())
