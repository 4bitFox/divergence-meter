import hw_nixie as n
import an_test as test
import an_divergence as divergence
import an_dt as dt




try:
    test.animation(0.5)
    divergence.animation()
    while True:
        dt.time()
        divergence.animation()
        dt.date()
        dt.misc()
        test.routine()
except BaseException as e:
    print("Error:", e)
finally:
    n.all_off()

