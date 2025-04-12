import board
import digitalio
import hw_ioexpander as ioexp
from hw_K155ID1 import outputs as Q




def setdigit(n, tube):
    if tube < 5:
        bus = 1
    else:
        bus = 2
        tube += -4 # for bus 2 start pin offset at 0 again
    
    offset = (tube - 1) * 4
    
    ioexp.set_pin(bus, 1 + offset, Q[n][0])
    ioexp.set_pin(bus, 2 + offset, Q[n][1])
    ioexp.set_pin(bus, 3 + offset, Q[n][2])
    ioexp.set_pin(bus, 4 + offset, Q[n][3])


def setdot(n, side="R"):
    if side == "R":
        RA.value = Q[n][0]
        RB.value = Q[n][1]
        RC.value = Q[n][2]
        RD.value = Q[n][3]
    else:
        LA.value = Q[n][0]
        LB.value = Q[n][1]
        LC.value = Q[n][2]
        LD.value = Q[n][3]



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

