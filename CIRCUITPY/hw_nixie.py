import board
import digitalio
import hw_ioexpander as ioexp
from hw_K155ID1 import outputs as Q




dots = {"R": None, "L": None}




def update():
    """
    display the pending changes on the nixies.
    """
    update_dot(dots["R"], "R")
    update_dot(dots["L"], "L")
    ioexp.update()


def set_digit(digit, tube):
    if tube < 5:
        bus = 1
    else:
        bus = 2
        tube += -4 # for bus 2 start pin offset at 0 again
    
    offset = (tube - 1) * 4
    
    ioexp.set_pin(bus, 1 + offset, Q[digit][0])
    ioexp.set_pin(bus, 2 + offset, Q[digit][1])
    ioexp.set_pin(bus, 3 + offset, Q[digit][2])
    ioexp.set_pin(bus, 4 + offset, Q[digit][3])


def set_dot(tube=None, side="R"):
    dots[side] = tube

def update_dot(tube=None, side="R"):
    if tube != None:
        tube += - 1

    if side == "R":
        RA.value = Q[tube][0]
        RB.value = Q[tube][1]
        RC.value = Q[tube][2]
        RD.value = Q[tube][3]
    else:
        LA.value = Q[tube][0]
        LB.value = Q[tube][1]
        LC.value = Q[tube][2]
        LD.value = Q[tube][3]

def all_off():
    ioexp.set_all(1)
    set_dot(None, "R")
    set_dot(None, "L")
    
    

# Left dots
LA = digitalio.DigitalInOut(board.GP19)
LA.direction = digitalio.Direction.OUTPUT
LB = digitalio.DigitalInOut(board.GP18)
LB.direction = digitalio.Direction.OUTPUT
LC = digitalio.DigitalInOut(board.GP17)
LC.direction = digitalio.Direction.OUTPUT
LD = digitalio.DigitalInOut(board.GP16)
LD.direction = digitalio.Direction.OUTPUT
# Right dots
RA = digitalio.DigitalInOut(board.GP12)
RA.direction = digitalio.Direction.OUTPUT
RB = digitalio.DigitalInOut(board.GP13)
RB.direction = digitalio.Direction.OUTPUT
RC = digitalio.DigitalInOut(board.GP14)
RC.direction = digitalio.Direction.OUTPUT
RD = digitalio.DigitalInOut(board.GP15)
RD.direction = digitalio.Direction.OUTPUT
