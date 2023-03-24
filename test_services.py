import unittest

import services as ser


class TestServices(unittest.TestCase):
    def test_task1(self) -> None:
        result = ser.get_hottest_day("lahore", 7)
        self.assertEqual(result, '{"day": "03/24/2023, 00:00:00", "temp_f": 64.8}')
        result = ser.get_hottest_day("lahore", 0)
        self.assertEqual(result, '{"error": "Something went wrong :("}')
        result = ser.get_hottest_day("karachi", 7)
        self.assertEqual(result, '{"day": "03/26/2023, 00:00:00", "temp_f": 73.8}')
        result = ser.get_hottest_day("karachi", 2)
        self.assertEqual(result, '{"day": "03/24/2023, 00:00:00", "temp_f": 73.6}')

    def test_task2(self) -> None:
        result = ser.second_most_humid_city()
        self.assertEqual(result, '{"city": "Islamabad", "avg_humidity": 71.33}')

    def test_task3(self) -> None:
        result = ser.city_with_lowest_daily_temp(3)
        self.assertEqual(result, '{"city": "Karachi", "avg_daily_tep_diff": 12.67}')
        result = ser.city_with_lowest_daily_temp(0)
        self.assertEqual(result, '{"city": "Karachi", "avg_daily_tep_diff": 7.9}')
        result = ser.city_with_lowest_daily_temp(1)
        self.assertEqual(result, '{"city": "Karachi", "avg_daily_tep_diff": 11.05}')

    def test_task4(self) -> None:
        result = ser.get_highest_temp_values("lahore")
        self.assertEqual(
            result,
            '{"day": "03/26/2023, 00:00:00", "max_temp_f": 86.2, "min_temp_f": 55.2, "difference": 31.0}',
        )


if __name__ == "__main__":
    unittest.main()
