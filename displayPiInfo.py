#!/usr/bin/env python

""" First version of PiInfo on display """

import sys
sys.path.append('/home/alesr/PythonDevelopment/SSD1306DisplayDriver/Driver/')

import oled
import piInfo.temp
import piInfo.sonarr
import piInfo.system

# init display to default values
oled.init(0,0x3C)
oled.cmdChargePumpEnable()
oled.cmdRemapCol(1)
oled.cmdRemapRow(1)
oled.cmdSetStartRow(0)
oled.cmdSetRowOffset(0)

# fetch information
curTemp = '{:4}'.format(str(piInfo.temp.CPU())+"C")
curSpace = '{:>4}'.format(str(piInfo.sonarr.diskSpace('media'))+"%")
upTimeStr = piInfo.system.upTimeAsDispStr()

# turn on display
oled.cmdDisplayON()
oled.cmdSetContrast(1)

# print basic info on yellow line
oled.printYelLn(curTemp+upTimeStr+curSpace)

# clear all blue lines (Issue#4)
for line in range(0,6):
    oled.printBluLn("",line)

# print episodes on blue lines
episodes = piInfo.sonarr.upcomingEp(7)
oled.printBluLn("UPCOMING EPISODES:",0,0)
for idx,ep in enumerate(episodes):
    if idx>5: break
    seriesTitle = '{:15}'.format(ep["seriesTitle"][:15])
    epNum = 'E'+'{:0>2}'.format(str(ep["episodeNumber"]))
    if ep["deltaDays"].days >=0:
        deltaDays = '+'+str(ep["deltaDays"].days)+'-'
    else:
        deltaDays = str(ep["deltaDays"].days)+'-'
    # check and show downloaded status
    if ep["hasFile"]:
        deltaDays = "* -"
    # check if isInQueue
    if piInfo.sonarr.isInQueue(ep["epid"]):
        deltaDays = "Q -"
    oled.printBluLn(deltaDays+seriesTitle+epNum,idx+1)

