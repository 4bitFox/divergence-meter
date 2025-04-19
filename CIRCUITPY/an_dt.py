import dt
import hw_nixie as n
from time import sleep
# (2, 0, 2, 5, 0, 3, 2, 9, 2, 0, 1, 4, 2, 8, 6, 1, 3, 0, 8, 8)
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19




def time():
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