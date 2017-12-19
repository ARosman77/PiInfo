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

time = piInfo.system.upTime()
print(str(time.seconds/3600))

upTime=int(time.total_seconds()//60)
if upTime > 99999:
    upTime=int(time.total_seconds()//3600)
    upTimeStr = str(upTime)+'h'
else:
    upTimeStr = str(upTime)+'m'

upTimeStr = '{:^6}'.format(upTimeStr)

print(upTimeStr)

