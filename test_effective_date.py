from datetime import *
from effective_date import get_effective_date
from unittest import TestCase

class TestEffectiveDate(TestCase):
    def test_today_is_working_monday_get_today(self):
        effective_date = get_effective_date(2016, 6, 27, 0)
        self.assertEqual(effective_date, date(2016,6,27))

    def test_today_is_sunday_get_monday(self):
        effective_date = get_effective_date(2016, 6, 26, 0)
        self.assertEqual(effective_date, date(2016, 6, 27))
    
    def test_today_is_saturday_get_monday(self):
        effective_date = get_effective_date(2016, 6, 25, 0)
        self.assertEqual(effective_date, date(2016, 6, 27))

    def test_today_is_working_monday_with_1_duration_get_tuesday(self):
        effective_date = get_effective_date(2016, 6, 27, 1)
        self.assertEqual(effective_date, date(2016, 6, 28))

    def test_today_is_sunday_with_1_duration_get_tuesday(self):
        effective_date = get_effective_date(2016, 6, 26, 1)
        self.assertEqual(effective_date, date(2016, 6, 28))

    def test_today_is_working_monday_with_2_duration_get_wensday(self):
        effective_date = get_effective_date(2016,6,27, 2)
        self.assertEqual(effective_date, date(2016,6,29))

    def test_today_is_saturday_with_1_duration_get_teusday(self):
        effective_date = get_effective_date(2016,6,25, 1)
        self.assertEqual(effective_date, date(2016,6,28))

    def test_today_is_saturday_with_3_duration_get_teusday(self):
        effective_date = get_effective_date(2016,6,25, 3)
        self.assertEqual(effective_date, date(2016,6,30))
