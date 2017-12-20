#!/usr/bin/env python
""" Test PiInfo package """

import piInfo.temp
import piInfo.sonarr
import piInfo.system
import requests

print(piInfo.temp.CPU())
print(str(piInfo.sonarr.diskSpace('media'))+'% free.')
episodes = piInfo.sonarr.upcomingEp(7)
for ep in episodes:
    print(str(ep["seriesTitle"]))

#time = piInfo.system.upTime()
# test limits
#from datetime import timedelta
#time = timedelta(0,134*3600+43*60) 
#print(time)

# show (xx min) until 59 min
#mode1Limit = 59*60
# show (xxx:xx) until 999h 59 min
#mode2Limit = 999*3600 + 59*60
# show (xxxxxh) else

#upTime=int(time.total_seconds()//60)
#upTime = int(time.total_seconds())
#if upTime <= mode1Limit:
#    upTimeStr = str(upTime//60)+' min'
#elif upTime <= mode2Limit:
#    upTimeStr = '{:0>2}'.format(str(upTime//3600)) \
#       + ':'+ '{:0>2}'.format(str((upTime%3600)//60))
#else:
#    upTimeStr = str(upTime//3600)+'h'
#
#upTimeStr = '{:^6}'.format(upTimeStr)

print(piInfo.system.upTimeAsDispStr())

