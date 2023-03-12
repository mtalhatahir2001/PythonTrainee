from typing import Any

import requests
from question_5 import WeatherForecaster


class Forecaster(WeatherForecaster):
    def __init__(self) -> None:
        self.__CURRENT_WEATHER_ROUTE = "/forecast.json"
        WeatherForecaster.__init__(self)

    def __fetch(self, url: str) -> dict:
        """
        This module/function fetch the api also filter the result based on self.__result_params
        """
        try:
            response = requests.get(url).json()
            result = dict()
            result["date_time"] = response.get("location").get("localtime")
            result["forecastday"] = list()
            for i in response.get("forecast").get("forecastday"):
                dayResult = dict()
                dayResult["daily_chance_of_rain"] = i.get("day").get(
                    "daily_chance_of_rain"
                )
                dayResult["daily_chance_of_snow"] = i.get("day").get(
                    "daily_chance_of_snow"
                )
                dayResult["condition"] = i.get("day").get("condition").get("text")
                for j in i.get("hour")[0]:
                    if j in self._WeatherForecaster__result_params:
                        dayResult[j] = i.get("hour")[0].get(j)
                air_quality_index = i.get("day").get("air_quality").get("us-epa-index")
                dayResult[
                    "air_quality"
                ] = self._WeatherForecaster__air_quality_types.get(air_quality_index)
                result["forecastday"].append(dayResult)
            return result
        except Exception as e:
            print(e)
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


print(Forecaster().get_forecast_data(True, hour=4, city="lahore", days=3))
