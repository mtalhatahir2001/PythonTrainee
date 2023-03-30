import logging
from typing import Any

import requests

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")


class WeatherForecaster:
    def __init__(self) -> None:
        self.__BASE_URL = "http://api.weatherapi.com/v1"
        self.__API_KEY = "e38e088af196452e88f145935230903"
        self.__CURRENT_WEATHER_ROUTE = "/current.json"
        self.__accepted_params = ["hour", "city", "postal_code", "days"]
        self.__priority_of_q = ["postal_code", "city"]
        self.__result_params = [
            "feelslike_f",
            "gust_mph",
            "humidity",
            "pressure_in",
            "cloud",
            "vis_km",
            "temp_f",
            "dewpoint_f",
        ]
        # Since weather api is only returning 1,2,3...
        # So created this hashtable for maping.
        self.__air_quality_types = {
            1: "Good",
            2: "Moderate",
            3: "Unhealthy for sensitive group",
            4: "Unhealthy",
            5: "Very Unhealthy",
            6: "Hazardous",
        }

    def __create_url(self, route_url: str, params: dict[str, Any]) -> str:
        """
        Takes all the params and returns the url that can directly be fetched.
        """
        url = f"{self.__BASE_URL}{route_url}?key={self.__API_KEY}"
        q = self.__get_value_of_q(params)
        if q != None:
            url += f"&q={q}"
        for i in params:
            if not i in self.__priority_of_q:
                url += f"&{i}={params[i]}"
        return url

    def __get_value_of_q(self, params: dict[str, Any]) -> Any:
        """
        Since q can have more then one value, this function resolves parameters into q
        based on priority. postal_code > city > country
        """
        for i in self.__priority_of_q:
            if params.get(i) != None:
                return params.get(i)
        return None

    def __fetch(self, url: str) -> dict:
        """
        This module/function fetch the api also filter the result based on self.__result_params
        """
        try:
            logging.info(f"fetching {url}")
            response = requests.get(url).json()
            result = dict()
            result["date_time"] = response.get("location").get("localtime")
            result["condition"] = response.get("current").get("condition").get("text")
            result["city"] = response.get("location").get("name")
            result["latitude"] = response.get("location").get("lat")
            result["longitude"] = response.get("location").get("lon")
            for i in response.get("current"):
                if i in self.__result_params:
                    result[i] = response.get("current").get(i)
            air_quality_index = (
                response.get("current").get("air_quality").get("us-epa-index")
            )
            result["air_quality"] = self.__air_quality_types.get(air_quality_index)
            return result
        except Exception as e:
            logging.exception("Exception")
            return dict()

    def get_current_weather(
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
        city : str
        postal_code : int
            If both city and postal_code are provided this fucntion will priortize search
        based on postal_code and will ignore all other params other then these.
        """
        # These line removes all the parameters that are not required by the API.
        filtered_params = dict()
        for i in extra_params:
            if i in self.__accepted_params:
                filtered_params[i] = extra_params[i]
        filtered_params["aqi"] = "yes" if air_quality else "no"

        url = self.__create_url(self.__CURRENT_WEATHER_ROUTE, filtered_params)
        return self.__fetch(url)
