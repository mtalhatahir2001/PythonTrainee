import logging

import services as ser

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")

if __name__ == "__main__":
    try:
        print(ser.get_hottest_day("karachi", 6))
        print(ser.second_most_humid_city())
        ser.dump_forecasted_data("islamabad", 7)
        ser.dump_current_data("islamabad")
        print(ser.get_highest_temp_values("islamabad"))
        print(ser.city_with_lowest_daily_temp(7))
    except Exception as e:
        logging.exception("Exception occured")
