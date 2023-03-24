import logging

from services import get_highest_temp_values

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")

if __name__ == "__main__":
    try:
        # print(get_hottest_day("karachi", 6))
        # print(second_most_humid_city())
        # dump_forecasted_data("islamabad", 7)
        # dump_current_data("islamabad")
        print(get_highest_temp_values("islamabad"))
        pass
    except Exception as e:
        logging.exception("Exception occured")
