import usb_cdc
import hw_nixie as n
from time import sleep



serial = usb_cdc.console
_buf = bytearray()
def read_serial():
    global _buf

    if serial.in_waiting == 0:
        return None

    data = serial.read(serial.in_waiting)
    if not data:
        return None

    _buf.extend(data)

    if b"\n" not in _buf: # when no newline has arrived
        return None
    
    lines = _buf.split(b"\n")
    line = lines[-2] # Last complete line
    _buf = bytearray(lines[-1]) # keep incomplete line
    
    instructions = eval(line.decode().strip())
    return instructions



def run_instructionlist():
    """
    Will read an instructionlist from Serial.
    Example: [[[None, 0, 1, 2, 3, 4, 5, 6], [None, 2], 2],
              [[None, None, None, None, None, None, None, None], [None, None], 0]]
              will display on the tubes _1.23456 for 2 seconds, then clear all tubes.
            
             [[[tube_states], [dot_state_left, dot_state_right], duration], ...]
    """
    try:
        serial_input = read_serial()
        if serial_input:
            print(str(serial_input))
            for instruction in serial_input:
                tube_states = instruction[0]
                dot_states = instruction[1]
                duration = instruction[2]
                for tube in range(1, 9):
                    n.set_digit(tube_states[tube - 1], tube)
                n.set_dot(dot_states[0], "L")
                n.set_dot(dot_states[1], "R")
                n.update()
                sleep(duration)
    except BaseException as e:
        print("(╥﹏╥)    SERIAL ERROR:", e)
        n.all_off()
        n.update()
    finally:
        return
