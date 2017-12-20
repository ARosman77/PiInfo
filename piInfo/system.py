""" System info """

from datetime import timedelta

def upTime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        result = timedelta(seconds = uptime_seconds)
    return result

def upTimeAsDispStr():
    # show (xx min) until 59 min
    mode1Limit = 59*60
    # show (xxx:xx) until 999h 59 min
    mode2Limit = 999*3600 + 59*60
    # show (xxxxxh) else
    time = int(upTime().total_seconds())
    if time <= mode1Limit:
        upTimeStr = str(time//60)+' min'
    elif time <= mode2Limit:
        upTimeStr = '{:0>2}'.format(str(time//3600)) \
            + ':'+ '{:0>2}'.format(str((time%3600)//60))
    else:
        upTimeStr = str(time//3600)+'h'
    upTimeStr = '{:^6}'.format(upTimeStr)
    return upTimeStr
