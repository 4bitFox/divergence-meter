import adafruit_datetime as dt
import time


def tuple_of_digits(struct_time):
    """
    returns a tuple like (2, 0, 2, 5, 0, 3, 2, 9, 2, 0, 1, 4, 2, 8, 1, 3, 6, 0, 8, 8)
                          Y  Y  Y  Y  M  M  D  D  h  h  m  m  s  s  cw cw wd yd yd yd
    """
    weekday = _weekday(struct_time)
    calendar_week = _calendar_week(struct_time)
    day_of_year = _day_of_year(struct_time)
    string_time = f"{struct_time.tm_year:04}{struct_time.tm_mon:02}{struct_time.tm_mday:02}{struct_time.tm_hour:02}{struct_time.tm_min:02}{struct_time.tm_sec:02}{calendar_week:02}{weekday:01}{day_of_year:03}"
    digits = []
    for digit in string_time:
        digits.append(int(digit))
    return tuple(digits)

def _weekday(struct_time):
    """
    Returns the weekday starting from 1
    """
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day_of_month = struct_time.tm_mday
    return dt.date(year, month, day_of_month).isoweekday()
    

def _first_weekday_of_year(struct_time):
    """
    Returns the weekday. Starts with 1 being Monday
    """
    year = struct_time.tm_year
    first_weekday_of_year = dt.date(year, 1, 1).isoweekday()
    return first_weekday_of_year

def _day_of_year(struct_time):
    """
    Returns the day of the month. Starts with 1
    """
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day_of_month = struct_time.tm_mday
    # calculate day of year
    day_of_year = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1]) + day_of_month
    # account for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if month > 2:
            day_of_year += 1
    return day_of_year
    

def _calendar_week(struct_time):
    """
    Returns the calendar week starting from 1
    """
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day_of_month = struct_time.tm_mday
    
    first_weekday_of_year = _first_weekday_of_year(struct_time)
    day_of_year = _day_of_year(struct_time)
    weekday = _weekday(struct_time)

    # Calculate the calendar week number
    calendar_week = (day_of_year + first_weekday_of_year - 1 + (7 - weekday)) // 7

    return calendar_week

