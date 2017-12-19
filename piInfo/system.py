""" System info """

from datetime import timedelta

def upTime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        result = timedelta(seconds = uptime_seconds)
    return result
