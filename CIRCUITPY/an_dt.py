import os
import dt
import hw_nixie as n
from time import sleep
# (2, 0, 2, 5, 0, 3, 2, 9, 2, 0, 1, 4, 2, 8, 6, 1, 3, 0, 8, 8)
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19




def time():
    """
    Displays current time accureate to the second until the next minute starts.
    """
    d_prev = None
    dot_pos_1 = "R"
    dot_pos_2 = "L"
    while True:
        d = dt.get_dt_tuple()
        if d[12] == 0 and d[13] == 0:
            n.all_off()
            return
        if d != d_prev:
            n.set_digit(d[8], 1)
            n.set_digit(d[9], 2)
            n.set_dot(3, dot_pos_1)
            n.set_digit(d[10], 4)
            n.set_digit(d[11], 5)
            n.set_dot(6, dot_pos_2)
            n.set_digit(d[12], 7)
            n.set_digit(d[13], 8)
            d_prev = d
            if dot_pos_1 == "R":
                dot_pos_1 = "L"
                dot_pos_2 = "R"
            else:
                dot_pos_1 = "R"
                dot_pos_2 = "L"
            n.update()
        sleep(0.01)

def date(duration=3):
    """
    Displays date.
    """
    d = dt.get_dt_tuple()
    n.set_digit(d[6], 1)
    n.set_digit(d[7], 2)
    n.set_dot(2, "R")
    n.set_digit(d[4], 3)
    n.set_digit(d[5], 4)
    n.set_dot(5, "L")
    n.set_digit(d[0], 5)
    n.set_digit(d[1], 6)
    n.set_digit(d[2], 7)
    n.set_digit(d[3], 8)
    n.update()
    sleep(duration)
    n.all_off()

def misc(duration=3):
    """
    Displays weekday, calendar week and day of year.
    """
    d = dt.get_dt_tuple()
    n.set_digit(d[14], 1)
    n.set_digit(d[15], 3)
    n.set_digit(d[16], 4)
    n.set_digit(d[17], 6)
    n.set_digit(d[18], 7)
    n.set_digit(d[19], 8)
    n.update()
    sleep(duration)
    n.all_off()
    
def ntp_sync(force=False):
    """
    Sync time with ntp server when it is currently the time specified in settings.toml NTP_DAILY_SYNC_TIME or when force=True
    """
    d = dt.get_dt_tuple()

    sync_time_str = os.getenv("NTP_DAILY_SYNC_TIME")
    sync_time_tuple = (int(sync_time_str[0]), int(sync_time_str[1]), int(sync_time_str[3]), int(sync_time_str[4]))
    
    if d[8] == sync_time_tuple[0] and d[9] == sync_time_tuple[1] and d[10] == sync_time_tuple[2] and d[11] == sync_time_tuple[3] or force:
        for attempts in range(3):
            for dot_cycles in range(3):
                for dot_pos in range(1, 5):
                    n.set_dot(5 - dot_pos, "R")
                    n.set_dot(4 + dot_pos, "L")
                    n.update()
                    sleep(0.2)
            n.all_off()
            status = dt.set_dt_ntp()
            if status:
                break
        if status == True:
            for i in range(3):
                if i == 2:
                    date(duration=2)
                else:
                    date(duration=0.5)
                n.all_off()
                sleep(0.2)
        elif status == False:
            for i in range(3):
                for tube in range(1, 9):
                    n.set_digit(0, tube)
                n.update()
                if i == 2:
                    sleep(2)
                else:
                    sleep(0.5)
                n.all_off()
                sleep(0.2)
