import logging

from services import get_hottest_day

logging.basicConfig(level=logging.DEBUG, filename="logs.txt")

if __name__ == "__main__":
    try:
        print(get_hottest_day("karachi", 6))
    except Exception as e:
        logging.exception("Exception occured")
