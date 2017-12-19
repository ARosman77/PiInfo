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

test = '{:>10}'.format(str(time.seconds/3600))

print(test)

