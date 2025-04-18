import hw_rtc as rtc
import hw_nixie as n
import dt
import an_test as test
import an_divergence as divergence


struct_time = rtc.get_struct_time()
d = dt.tuple_of_digits(struct_time)
print(d)




try:
    test.animation(0.5)
    while True:
        divergence.animation()
except BaseException as e:
    print("Error:", e)
finally:
    n.all_off()
