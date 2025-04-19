import hw_nixie as n
import an_test
import an_divergence
import an_dt
import dt




try:
    an_test.animation(0.5)
    an_divergence.animation()
    while True:
        an_dt.time()
        an_divergence.animation()
        an_dt.date()
        an_dt.misc()
        an_test.routine()
        dt.sync_ntp_routine()
except BaseException as e:
    print("CRITICAL ERROR:", e)
finally:
    n.all_off()

