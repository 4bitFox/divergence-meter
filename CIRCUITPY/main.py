import hw_nixie as n
import an_test
import an_divergence
import an_dt
from time import sleep




try:
    an_test.animation(0.5)
    sleep(1)
    an_divergence.animation()
    sleep(1)
    an_dt.ntp_sync(force=True)
    while True:
        an_dt.time()
        an_divergence.animation()
        an_dt.date()
        an_dt.misc()
        
        # routines
        an_test.routine()
        an_dt.ntp_sync()
except BaseException as e:
    print("CRITICAL ERROR:", e)
finally:
    n.all_off()

