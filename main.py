import logging

from services import get_hottest_day, second_most_humid_city

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")

if __name__ == "__main__":
    try:
        # print(get_hottest_day("islamabad", 6))
        print(second_most_humid_city())
    except Exception as e:
        logging.exception("Exception occured")
