import hw_rtc as rtc
import dt


struct_time = rtc.get_struct_time()
d = dt.tuple_of_digits(struct_time)
print(d)



import hw_nixie as n
from time import sleep

def test(t = 1):
    dot_pos = 1
    while True:
        for digit in range(0, 11):
            if digit == 10:
                for tube in range(1, 9):
                    n.set_digit(None, tube)
            else:
                for tube in range(1, 9):
                    print(digit, tube)
                    n.set_digit(digit, tube)
            
            n.set_dot(dot_pos, "R")
            n.set_dot(dot_pos, "L")
            if dot_pos == None:
                dot_pos = 1
            else:
                dot_pos += 1
            if dot_pos > 8:
                dot_pos = None
            
            n.update()
            sleep(t)


try:
    test()
except BaseException as e:
    n.all_off()
    print(e)
