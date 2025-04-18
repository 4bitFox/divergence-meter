import hw_nixie as n
from time import sleep, monotonic
import random


last_divergence = "0.000000"

def display(divergence):
    if "." not in divergence:
        n.set_dot(None, "R")
    for tube in range(1, 9):
        value = divergence[tube - 1]
        if value == ".":
            n.set_dot(tube, "R")
            n.set_digit(None, tube)
        else:
            value = int(value)
            n.set_digit(value, tube)
    n.update()


def animation(divergence=None, beginning_sleep=1, end_sleep=3, loop_sleep=0.012, fix_interval=0.3):
    global last_divergence
    display(last_divergence)
    sleep(beginning_sleep)
    
    if divergence == None:
        divergence_float = random.uniform(0.1, 2)
        divergence = f"{divergence_float:.8f}"
    
    fixed_digits = [False, False, False, False, False, False, False, False]
    time_refrence = monotonic()
    while True:
        time = monotonic()
        if time - time_refrence >= fix_interval:
            time_refrence = time
            while True:
                digit_to_fix = random.randint(0, 7)
                if fixed_digits[digit_to_fix] == False:
                    break
            fixed_digits[digit_to_fix] = True
            
        numbers = str(random.randint(10000000, 99999999))
        numbers_fixed_list = []
        for i, fixed_digot_bool in enumerate(fixed_digits):
            if fixed_digits[i]:
                if i == 1:
                    numbers_fixed_list.append(".")
                else:
                    numbers_fixed_list.append(divergence[i])
            else:
                numbers_fixed_list.append(numbers[i])
        numbers_fixed = "".join(numbers_fixed_list)
        display(numbers_fixed)
        if not False in fixed_digits:
            break
        sleep(loop_sleep)
    
    last_divergence = divergence
    sleep(end_sleep)