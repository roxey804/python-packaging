import pytest
import pendulum

from days_to_bday import days_to_bday


def test_days_to_bday():
  birthday = "02/02/2022"
  future_bday = pendulum.datetime(2021, 12, 15)
  today = pendulum.datetime(2021, 12, 13)
  assert days_to_bday.days_to_bday(birthday) == 49
