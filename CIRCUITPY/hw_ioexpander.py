import board
import busio

# i2c adresses
bus1 = 0x20
bus2 = 0x21

# Register addresses
CONFIG_REG = 0x06  # Configuration register (input/output)
OUTPUT_REG = 0x02  # Output register




class PCA9535:
    def __init__(self, i2c, address=bus1):
        self.i2c = i2c
        self.address = address
        self.output_state = [1] * 16  # Default all outputs high
        self._write_register(CONFIG_REG, 0x0000)  # Set all pins as output initially (output: 0x0000, input: 0xFFFF)
        self.update_output_register()

    def _write_register(self, reg, value):
        data = value.to_bytes(2, 'little')
        while not self.i2c.try_lock():
            pass
        self.i2c.writeto(self.address, bytes([reg]) + data)
        self.i2c.unlock()
        
    def update_output_register(self):
        output_value = sum([(1 << i) if self.output_state[i] else 0 for i in range(16)])
        self._write_register(OUTPUT_REG, output_value)

    def write_pin(self, pin, value):
        pin += -1 # shift start from 1 to 0
        if 0 <= pin < 16:
            self.output_state[pin] = 1 if value else 0
            self.update_output_register()
        else:
            raise Exception("Pin out of range!")




def set_pin(bus, pin, value):
    """
    Set pin high (True) or low (False)
    There is bus 1 and bus 2
    Pins range from 1 to 16
    """
    if bus == 1:
        bus = b1
    else:
        bus = b2
    bus.write_pin(pin, value)


def set_all(value):
    for bus in (b1, b2):
        bus.output_state = [value] * 16
        bus.update_output_register()

i2c = busio.I2C(scl=board.GP3, sda=board.GP2)

b1 = PCA9535(i2c, bus1)
b2 = PCA9535(i2c, bus2)

