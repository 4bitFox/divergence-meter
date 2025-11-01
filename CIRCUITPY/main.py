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
        an_dt.days_between_dates()
        
        # routines (these functions only run at specific times)
        an_test.routine() # Runs every hour to improve health of nixie tubes.
        an_dt.ntp_sync() # Runs daily at NTP_DAILY_SYNC_TIME (see settings.toml).
except BaseException as e:
    print("(╥﹏╥)    CRITICAL ERROR:", e)
finally:
    n.all_off()

