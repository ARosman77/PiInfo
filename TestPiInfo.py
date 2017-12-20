#!/usr/bin/env python
""" Test PiInfo package """

import piInfo.temp
import piInfo.sonarr
import piInfo.system
import requests

# test temperature readings
print("CPU temperature:" + str(piInfo.temp.CPU()) + 'C')
# test free disk space readings
print("Disk "+str(piInfo.sonarr.diskSpace('media'))+'% free.')
# test upTime for display command
print(piInfo.system.upTimeAsDispStr())
# test upcomming episodes list
episodes = piInfo.sonarr.upcomingEp(7)
for idx,ep in enumerate(episodes):
    seriesTitle = '{:15}'.format(ep["seriesTitle"][:15])
    epNum = 'E'+'{:0>2}'.format(str(ep["episodeNumber"]))
    if ep["deltaDays"].days >=0:
        deltaDays = '+'+str(ep["deltaDays"].days)+'-'
    else:
        deltaDays = str(ep["deltaDays"].days)+'-'
    print(deltaDays+seriesTitle+epNum)

