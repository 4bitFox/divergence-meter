# Divergence Meter

### Main Loop:

https://github.com/user-attachments/assets/454079d6-4c25-4eff-9755-33558b0b4115

- Display Time
- Every Minute:
  - Divergence animation
  - Display Date
  - Display Misc. (Weekday, ISO Calendar Week, Day of Year)
- Every Hour:
  - Cycle all digits (anti cathode poisoning routine)
- Every Day:
  - NTP network time-sync (at 03:30)

### Startup Sequence:

https://github.com/user-attachments/assets/f7f01907-7353-47da-a86c-e9c85c2cbf1e

- Cycle all digits (selftest & anti cathode poisoning routine)
- Divergence animation
- NTP network time-sync
- -> Start main loop




## Components I used:
- 1x Raspberry Pi Pico 2W
- 10x [K115ID1](https://www.aliexpress.com/item/1005002014120520.html)
- 1x [DS3231 AT24C32 RTC Module](https://www.aliexpress.com/item/32533518502.html)
- 8x [Nixie Indicator Tubes IN-14 (0-9 and 2 dots)](https://soviet-tubes.com/product/in-14-nixie-tube/)
- 8x [Resistor (In my case 10 kΩ)](https://www.aliexpress.com/item/32847096736.html)
- 1x [5V to 170V Boost Converter for Nixies](https://www.aliexpress.com/item/1005005899219043.html)
