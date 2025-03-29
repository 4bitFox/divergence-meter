import time


def struct_time_to_tuple_of_digits(struct_time):
    """
    returns a tuple like (2, 0, 2, 5, 0, 3, 2, 9, 2, 0, 1, 4, 2, 8, 6, 1, 3)
                          Y  Y  Y  Y  M  M  D  D  h  h  m  m  s  s  wd cw cw
    """
    calendar_week = calculate_calendar_week(struct_time)
    string_time = f"{struct_time.tm_year:04}{struct_time.tm_mon:02}{struct_time.tm_mday:02}{struct_time.tm_hour:02}{struct_time.tm_min:02}{struct_time.tm_sec:02}{struct_time.tm_wday + 1}{calendar_week:02}"
    digits = []
    for digit in string_time:
        digits.append(int(digit))
    return tuple(digits)


def calculate_calendar_week(struct_time): # Untested ChatGPT code

    # Extract year, month, and day
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day = struct_time.tm_mday

    # Calculate the first day of the year (January 1st)
    first_day_of_year = time.struct_time((year, 1, 1, 0, 0, 0, 0, 0, -1))

    # Calculate the weekday of January 1st (0=Monday, 6=Sunday)
    first_day_weekday = first_day_of_year.tm_wday

    # Calculate the day of the year for the current date
    day_of_year = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1]) + day

    # Adjust for leap year if necessary
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if month > 2:
            day_of_year += 1

    # Calculate the day of the week for the current date
    current_weekday = (first_day_weekday + day_of_year - 1) % 7

    # Calculate the calendar week number
    calendar_week = (day_of_year + (7 - current_weekday)) // 7

    return calendar_week
