import hw_nixie as n
from time import sleep




def animation_loop(t = 1):
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


def animation(t = 1):
    dot_pos = 1
    for digit in range(0, 11):
        if digit == 10:
            for tube in range(1, 9):
                n.set_digit(None, tube)
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
