#!/usr/bin/env python

""" First version of PiInfo on display """

import sys
sys.path.append('/home/alesr/PythonDevelopment/SSD1306DisplayDriver/Driver/')

import oled
import piInfo.temp
import piInfo.sonarr
import piInfo.system

oled.init(0,0x3C)
oled.cmdChargePumpEnable()
oled.cmdRemapCol(1)
oled.cmdRemapRow(1)
oled.cmdSetStartRow(0)
oled.cmdSetRowOffset(0)

curTemp = '{:4}'.format(str(piInfo.temp.CPU())+"C")
curSpace = '{:>4}'.format(str(piInfo.sonarr.diskSpace('media'))+"%")
#upTime = '{:^6}'.format(str(int(piInfo.system.upTime().total_seconds()//3600))+"h")
upTimeStr = piInfo.system.upTimeAsDispStr()

oled.cmdDisplayON()
oled.cmdSetContrast(1)

oled.printYelLn(curTemp+upTimeStr+curSpace)

episodes = piInfo.sonarr.upcomingEp(7)
oled.printBluLn("UPCOMING EPISODES:",0,0)
for idx,ep in enumerate(episodes):
    if idx>5: break
    oled.printBluLn(ep["seriesTitle"]+"-"+str(ep["episodeNumber"]),idx+1,0)
