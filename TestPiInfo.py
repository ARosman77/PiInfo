#!/usr/bin/env python
""" Test PiInfo package """

import piInfo.temp
import piInfo.sonarr
import requests

print(piInfo.temp.CPU())
print(str(piInfo.sonarr.diskSpace('media'))+'% free.')
episodes = piInfo.sonarr.upcomingEp(7)
for ep in episodes:
    print(str(ep["seriesTitle"]))

