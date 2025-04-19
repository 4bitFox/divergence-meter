import os
import wifi
import time
import adafruit_ntp
import adafruit_connection_manager


def _connect(wifi_ssid = os.getenv("WIFI_SSID"), wifi_password   = os.getenv("WIFI_PASSWORD")):
    if wifi.radio.connected is False:
        wifi.radio.connect(wifi_ssid, wifi_password)

def _disconnect():
    wifi.radio.enabled = False
    
def _ntp_struct_time(tz_offset):
    pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
    ntp = adafruit_ntp.NTP(pool, tz_offset=tz_offset, cache_seconds=3600)
    return ntp.datetime

def get_ntp_struct_time(tz_offset=os.getenv("TZ_OFFSET")):
    try:
        _connect()
        struct_time = _ntp_struct_time(tz_offset)
        _disconnect()
        return struct_time
    except BaseException as e:
        print(e)
        return None
