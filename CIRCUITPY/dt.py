import adafruit_datetime as dt
import hw_rtc as rtc
import hw_wifi as wifi
import cpython_datetime as cdt
import time



def set_dt(struct_time=None, Y=None, M=None, D=None, h=None, m=None, s=None):
    if struct_time:
        rtc.set_dt_struct_time(struct_time)
    else:
        rtc.set_dt(Y, M, D, h, m, s)

def set_dt_input():
    Y = int(input("Input Year in YYYY: "))
    M = int(input("Input Month in MM: "))
    D = int(input("Input Day in DD: "))
    h = int(input("Input Hour in hh: "))
    m = int(input("Input Minutes in mm: "))
    s = int(input("Input Seconds in ss: "))
    
    set_dt(None, Y, M, D, h, m, s)
    print("Done!")
    
def set_dt_ntp():
    struct_time = wifi.get_ntp_struct_time()
    if struct_time != None:
        set_dt(struct_time)
        return True
    else:
        return False


def get_dt_struct_time():
    struct_time = rtc.get_struct_time()
    return struct_time


def get_dt_tuple():
    struct_time = get_dt_struct_time()
    d = tuple_of_digits(struct_time)
    return d

struct_time_prev = None
digits_prev = None
day_of_month_prev = None
weekday_prev = None
calendar_week_prev = None
day_of_year_prev = None

def tuple_of_digits(struct_time):
    """
    returns a tuple like (2, 0, 2, 5, 0, 3, 2, 9, 2, 0, 1, 4, 2, 8, 6, 1, 3, 0, 8, 8)
                          Y  Y  Y  Y  M  M  D  D  h  h  m  m  s  s  wd cw cw yd yd yd
    """
    global struct_time_prev, digits_prev, day_of_month_prev, weekday_prev, calendar_week_prev, day_of_year_prev
    
    # Compute new digits if necessary
    if struct_time != struct_time_prev:
        day_of_month = struct_time.tm_mday
        # Only calculate daily
        if day_of_month != day_of_month_prev:
            # Recalculate values
            weekday_var = weekday(struct_time)
            calendar_week_var = iso_calendar_week(struct_time)
            day_of_year_var = day_of_year(struct_time)
            # Store updated values
            day_of_month_prev = day_of_month
            weekday_prev = weekday_var
            calendar_week_prev = calendar_week_var
            day_of_year_prev = day_of_year_var
        else:
            # Use old values
            weekday_var = weekday_prev
            calendar_week_var = calendar_week_prev
            day_of_year_var = day_of_year_prev
    
        string_time = f"{struct_time.tm_year:04}{struct_time.tm_mon:02}{day_of_month:02}{struct_time.tm_hour:02}{struct_time.tm_min:02}{struct_time.tm_sec:02}{weekday_var:01}{calendar_week_var:02}{day_of_year_var:03}"
        digits = []
        for digit in string_time:
            digits.append(int(digit))
        digits = tuple(digits)
        digits_prev = digits
        struct_time_prev = struct_time
    else:
        # Use previous digits
        digits = digits_prev
    return digits

def weekday(struct_time=None, year=None, month=None, day_of_month=None):
    """
    Returns the weekday starting from 1
    """
    if struct_time:
        year = struct_time.tm_year
        month = struct_time.tm_mon
        day_of_month = struct_time.tm_mday
    return dt.date(year, month, day_of_month).isoweekday()
    

def first_weekday_of_year(struct_time):
    """
    Returns the weekday. Starts with 1 being Monday
    """
    year = struct_time.tm_year
    first_weekday_of_year = dt.date(year, 1, 1).isoweekday()
    return first_weekday_of_year

def leap_year(struct_time=None, year=None):
    """
    Return True when leap year
    """
    if year == None:
        year = struct_time.tm_year
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def day_of_year(struct_time):
    """
    Returns the day of the year. Starts with 1
    """
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day_of_month = struct_time.tm_mday
    # calculate day of year
    day_of_year = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1]) + day_of_month
    # account for leap year
    if leap_year(year=year):
        if month > 2:
            day_of_year += 1
    return day_of_year

def iso_calendar_week(struct_time):
    """
    Return ISO calendar week
    """
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day = struct_time.tm_mday
    
    week1monday = cdt._isoweek1monday(year)
    today = cdt._ymd2ord(year, month, day)
    # Internally, week and day have origin 0
    week, day = divmod(today - week1monday, 7)
    if week < 0:
        year -= 1
        week1monday = cdt._isoweek1monday(year)
        week, day = divmod(today - week1monday, 7)
    elif week >= 52:
        if today >= cdt._isoweek1monday(year+1):
            year += 1
            week = 0
    return week+1

def days_between_dates(struct_time1=None, struct_time2=None, Y1=None, M1=None, D1=None, Y2=None, M2=None, D2=None):
    """
    Returns the number of days between two dates.
    """
    if struct_time1 != None:
        Y1 = struct_time1.tm_year
        M1 = struct_time1.tm_mon
        D1 = struct_time1.tm_mday

    if struct_time2 != None:
        Y2 = struct_time2.tm_year
        M2 = struct_time2.tm_mon
        D2 = struct_time2.tm_mday

    datetime1 = dt.datetime(Y1, M1, D1)
    datetime2 = dt.datetime(Y2, M2, D2)
    datetime_delta = datetime2 - datetime1
    delta = datetime_delta.days
    return delta
