from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Day(Base):
    __tablename__ = "Day"

    id: Mapped[int] = mapped_column(primary_key=True)
    day_date: Mapped[datetime] = mapped_column(DateTime())
    is_current: Mapped[bool] = mapped_column(Boolean())
    temprature_child: Mapped["Temprature"] = relationship(back_populates="day")
    wind_child: Mapped["Wind"] = relationship(back_populates="day")
    location_child: Mapped["Location"] = relationship(back_populates="day")
    condition_child: Mapped["Condition"] = relationship(back_populates="day")


class Temprature(Base):
    __tablename__ = "Temprature"

    id: Mapped[int] = mapped_column(primary_key=True)
    day_id: Mapped[int] = mapped_column(ForeignKey("Day.id"))
    day: Mapped[Day] = relationship(back_populates="temprature_child")
    temp_f: Mapped[float] = mapped_column(Float())
    feelslike_f: Mapped[float] = mapped_column(Float())


class Wind(Base):
    __tablename__ = "Wind"
    id: Mapped[int] = mapped_column(primary_key=True)
    day_id: Mapped[int] = mapped_column(ForeignKey("Day.id"))
    day: Mapped[Day] = relationship(back_populates="wind_child")
    vis_km: Mapped[float] = mapped_column(Float())
    gust_mph: Mapped[float] = mapped_column(Float())
    humidity: Mapped[int] = mapped_column(Integer())


class Location(Base):
    __tablename__ = "Location"

    id: Mapped[int] = mapped_column(primary_key=True)
    day_id: Mapped[int] = mapped_column(ForeignKey("Day.id"))
    day: Mapped[Day] = relationship(back_populates="location_child")
    longitude: Mapped[float] = mapped_column(Float())
    latitude: Mapped[float] = mapped_column(Float())
    name: Mapped[str] = mapped_column(String(32))


class Condition(Base):
    __tablename__ = "Condition"

    id: Mapped[int] = mapped_column(primary_key=True)
    day_id: Mapped[int] = mapped_column(ForeignKey("Day.id"))
    day: Mapped[Day] = relationship(back_populates="condition_child")
    daily_chance_of_rain: Mapped[int] = mapped_column(Integer(), nullable=True)
    daily_chance_of_snow: Mapped[int] = mapped_column(Integer(), nullable=True)
    condition: Mapped[str] = mapped_column(String(50))
    pressure_in: Mapped[float] = mapped_column(Float())
    cloud: Mapped[int] = mapped_column(Integer())
    dewpoint_f: Mapped[float] = mapped_column(Float(), nullable=True)
    air_quality: Mapped[str] = mapped_column(String())
