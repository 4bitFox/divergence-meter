# Divergence Meter

![vlcsnap-2025-05-03-15h28m24s842](https://github.com/user-attachments/assets/3e7c3a4f-3c39-4b51-9f8e-2aedccd4a3fe)

## Features:

### Main Loop:

- Display Time
- Every Minute:
  - Divergence animation
  - Display Date
  - Display Misc. (Weekday, ISO Calendar Week, Day of Year)
- Every Hour:
  - Cycle all digits (anti cathode poisoning routine)
- Every Day:
  - NTP network time-sync (at 03:30)
 
https://github.com/user-attachments/assets/454079d6-4c25-4eff-9755-33558b0b4115

### Startup Sequence:

- Cycle all digits (selftest & anti cathode poisoning routine)
- Divergence animation
- NTP network time-sync
  - Displays date when sync successfull, otherwise will display all zeros. Date and Time can be set manually with `import dt`, then `dt.set_dt_input()` (manual input in terminal) or `dt.set_dt(Y, M, D, h, m, s)` (pass datetime values on function call). For that you can use e.g. [Thonny](https://thonny.org/).
- -> Start main loop

https://github.com/user-attachments/assets/f7f01907-7353-47da-a86c-e9c85c2cbf1e

## Components I used:
- 1x Raspberry Pi Pico 2W
- 10x [K115ID1](https://www.aliexpress.com/item/1005002014120520.html)
- 1x [DS3231 AT24C32 RTC Module](https://www.aliexpress.com/item/32533518502.html)
- 1x [IO Zero 32 (2x PCA9535)](https://www.abelectronics.co.uk/p/86/io-zero-32)
- 8x [Nixie Indicator Tubes IN-14 (0-9 and 2 dots)](https://soviet-tubes.com/product/in-14-nixie-tube/)
- 8x [Resistor (In my case 10 kΩ)](https://www.aliexpress.com/item/32847096736.html)
- 1x [5V to 170V DC Boost Converter for Nixies](https://www.aliexpress.com/item/1005005899219043.html) (See High Voltage waring below!)

## Wiring:

> [!CAUTION]
> We are working with HIGH VOLTAGE here, you have to know what you are doing! I'm not responsibe for anything that might happen! Be careful and don't get yourself or others hurt!

I don't want to specify this everywhere but I'll say it just in case; For all the components also wire them up to 5V and GND so they can work. :-D

### GPIO on the Pico:

GPIO Pins can be changed in the hw_ files if needed.

DS3231 RTC:
- SDA: GP0
- SCL: GP1

IO Zero 32 (PCA9535):
- SDA: GP2
- SCL: GP3

K115ID1:
- for Right Dots:
  - A: GP12
  - B: GP13
  - C: GP14
  - D: GP15
- for Left Dots:
  - A: GP19
  - B: GP18
  - C: GP17
  - D: GP16
 
### GPIO on the IO Zero 32 (2x PCA9535):

Use the pins on the IO-Expander, not the Pico here!

K115ID1:
- Bus 1 (on IO Zero 32):
  - for Tube 1:
    - A: Pin1
    - B: Pin2
    - C: Pin3
    - D: Pin4
  - for Tube 2:
    - A: Pin5
    - B: Pin6
    - C: Pin7
    - D: Pin8
  - for Tube 3:
    - A: Pin9
    - B: Pin10
    - C: Pin11
    - D: Pin12
  - for Tube 4:
    - A: Pin13
    - B: Pin14
    - C: Pin15
    - D: Pin16
- Bus 2 (on IO Zero 32):
  - for Tube 5:
    - A: Pin1
    - B: Pin2
    - C: Pin3
    - D: Pin4
  - for Tube 6:
    - A: Pin5
    - B: Pin6
    - C: Pin7
    - D: Pin8
  - for Tube 7:
    - A: Pin9
    - B: Pin10
    - C: Pin11
    - D: Pin12
  - for Tube 8:
    - A: Pin13
    - B: Pin14
    - C: Pin15
    - D: Pin16

### Nixie Tubes:

Wire the 170V source to the Anode to the Tube. Don't forget the resistor inbetween!!

Make sure to plan out how you wanna wire the Nixies, as it's probably going to get extremely cramped! See this before and after:

![Screenshot From 2025-05-04 14-09-56](https://github.com/user-attachments/assets/ed8f835f-f115-463c-8f0a-ab7fd842631f)
![Screenshot From 2025-05-04 14-12-50](https://github.com/user-attachments/assets/726187fe-5b2d-4aaf-9a47-201f173a326e)

Left (or upper) image has all the left dots wired and working as well as all the digits of the first tube, right (or lower) image is everything wired completely. I know it's not pretty and yes this took 4ever!

#### Digits:

The Pins for the digits will be wired to the K115ID1 that is wired to the IO Zero 32 (2x PCA9535). Use the datasheet as refrence. 

#### Dots:

The pins for the dots will be wired to the K115ID1 that are wired to the Pico 2W. The dots of the 1st tube for example will be wired to output 0 of the corresponding left/right K115ID1. Then the 2nd tube with output 1, and so on...

### Notes:
Note that the 8x K115ID1 wired to the IO Zero 32 (2x PCA9535) are used for all 8 nixie tubes to display the dots 0-9. Only one digit per tube can be lit at a given time! 
The left and right dots are controlled by 2x K115ID1 wired to the Pico 2W. The dot is decimal shifted between the tubes, meaning e.g the right dot can only be lit in one of the eight tubes at one time, same for the left! Keep this in mind if you want to write code yourself with this wiring, otherwise you can ignore this!

## Installation:

- Go to the [releases](https://github.com/4bitFox/divergence-meter/releases) and download the files (source files are not needed).
- Put the circuitpython uf2 onto the root of the pico. It will flash CircuitPython...
  - If you need to reflash use the flash_nuke.uf2 and then do the above step. Beware that this deletes everything you have on the pico curently!
- Copy/Move the contents of the unpacked CIRCUITPY.zip onto the pico. if you didn't rename the FAT32 pertition, it should show up as CIRCUITPY.
- If you power the Pico, boot.py and main.py should start running.

### Dependencies:

If you clone the repo and don't use the releases version you need to add some dependencies into the lib/ folder on the Pico with CircuitPython (or use the lib/ folder drom inside the CIRCUITPY.zip):
- adafruit-circuitpython-connectionmanager
- adafruit-circuitpython-datetime
- adafruit-circuitpython-ds3231
- adafruit-circuitpython-ntp
- adafruit-circuitpython-register
 
## Helpful Datasheets/Websites:
- [K115ID1](https://tubehobby.com/datasheets/k155id1.pdf)
- [GAZOTRON IN-14](https://www.tube-tester.com/sites/nixie/data/in-14/in-14.htm)
