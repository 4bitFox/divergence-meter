import hw_rtc as rtc
import dt


struct_time = rtc.get_struct_time()
d = dt.tuple_of_digits(struct_time)
print(d)
