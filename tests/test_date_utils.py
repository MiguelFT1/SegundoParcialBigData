import datetime as dt
import holidays

def date_key_from_date(d: dt.date) -> int:
    return int(d.strftime("%Y%m%d"))

def test_date_key():
    assert date_key_from_date(dt.date(2005, 12, 1)) == 20051201
    assert date_key_from_date(dt.date(2025, 1, 9)) == 20250109

def test_us_holiday_sample():
    us = holidays.US(years=[2025])
    assert dt.date(2025, 7, 4) in us