import os
import supervisor

VID = os.getenv("VENDOR_ID")
PID = os.getenv("PRODUCT_ID")
PRODUCT_NAME = os.getenv("PRODUCT_NAME")
MANUFACTURER_NAME = os.getenv("MANUFACTURER_NAME")

# Set USB identification
supervisor.set_usb_identification(vid=VID, pid=PID, manufacturer=MANUFACTURER_NAME, product=PRODUCT_NAME)
