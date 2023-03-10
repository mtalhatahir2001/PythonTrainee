import requests


def get_current_weather() -> str:
    print(
        requests.get(
            "http://api.weatherapi.com/v1/current.json?key=e38e088af196452e88f145935230903&q=lahore"
        ).json()
    )


get_current_weather()
