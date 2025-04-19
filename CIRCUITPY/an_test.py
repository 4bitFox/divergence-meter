import hw_nixie as n
import dt
from time import sleep, monotonic




def animation_loop(t=0.5, duration=None):
    if duration != None:
        time_reference = monotonic()
    
    dot_pos = 1
    while True:
        for digit in range(0, 11):
            if digit == 10:
                for tube in range(1, 9):
                    n.set_digit(None, tube)
            else:
                for tube in range(1, 9):
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
        
        if duration != None:
                time = monotonic()
                if time - time_reference >= duration:
                    n.all_off()
                    return


def animation(t=0.5):
    dot_pos = 1
    for digit in range(0, 11):
        if digit == 10:
            n.all_off()
        else:
            for tube in range(1, 9):
                n.set_digit(digit, tube)
        
        n.set_dot(dot_pos, "R")
        n.set_dot(dot_pos, "L")
        if dot_pos != None:
            dot_pos += 1
            if dot_pos > 8:
                dot_pos = None
        
        n.update()
        sleep(t)


def routine():
    """
    If end of hour is detected, cycle trough all elements as routine
    """
    d = dt.get_dt_tuple()
    if d[10] == 5 and d[11] == 1:
        animation_loop(t=0.5, duration=60)

