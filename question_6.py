import logging
from typing import Any

import requests
from question_5 import WeatherForecaster

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")


class Forecaster(WeatherForecaster):
    def __init__(self) -> None:
        self.__CURRENT_WEATHER_ROUTE = "/forecast.json"
        WeatherForecaster.__init__(self)

    def __fetch(self, url: str) -> dict:
        """
        This module/function fetch the api also filter the result based on self.__result_params
        """
        try:
            logging.info(f"fetching {url}")
            response = requests.get(url).json()
            result = dict()
            result["date_time"] = response.get("location").get("localtime")
            result["city"] = response.get("location").get("name")
            result["latitude"] = response.get("location").get("lat")
            result["longitude"] = response.get("location").get("lon")
            result["forecastday"] = list()
            for i in response.get("forecast").get("forecastday"):
                dayResult = dict()
                dayResult["date"] = i.get("date")
                dayResult["daily_chance_of_rain"] = i.get("day").get(
                    "daily_chance_of_rain"
                )
                dayResult["daily_chance_of_snow"] = i.get("day").get(
                    "daily_chance_of_snow"
                )
                dayResult["maxtemp_f"] = i.get("day").get("maxtemp_f")
                dayResult["mintemp_f"] = i.get("day").get("mintemp_f")
                dayResult["condition"] = i.get("day").get("condition").get("text")
                for j in i.get("hour")[0]:
                    if j in self._WeatherForecaster__result_params:
                        dayResult[j] = i.get("hour")[0].get(j)
                air_quality_index = i.get("day").get("air_quality")
                if air_quality_index != None:
                    air_quality_index = air_quality_index.get("us-epa-index")
                else:
                    air_quality_index = -1
                dayResult[
                    "air_quality"
                ] = self._WeatherForecaster__air_quality_types.get(air_quality_index)
                result["forecastday"].append(dayResult)
            return result
        except Exception as e:
            logging.exception("Exception")
            return dict()

    def get_forecast_data(
        self, air_quality: bool = False, **extra_params: dict[str, Any]
    ) -> dict:
        """
        Fetch the weather api based on the parameters provided.\n
        Required parameters
        -------------------
        air_quality : bool
            Default value is False\n
        Optional parameters
        -------------------
        hour : int
            24 hour format
        days: int
            number of days to strict your result.
        city : str
        postal_code : int
            If both city and postal_code are provided this fucntion will priortize search
        based on postal_code and will ignore all other params other then these.
        """
        filtered_params = dict()
        for i in extra_params:
            if i in self._WeatherForecaster__accepted_params:
                filtered_params[i] = extra_params[i]
        filtered_params["aqi"] = "yes" if air_quality else "no"
        url = self._WeatherForecaster__create_url(
            self.__CURRENT_WEATHER_ROUTE, filtered_params
        )
        return self.__fetch(url)
