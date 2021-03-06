""" Get info from Sonarr API """

import requests
import time
from datetime import date
from datetime import timedelta
from datetime import datetime

API_KEY='4b4a58ddaccd47718596a0b52a3427f9'
API_BASE='http://localhost:8989/api'
headers = { 'X-Api-Key': API_KEY }

def sendReq(endpoint,*params):
    addr=API_BASE+'/'+endpoint
    index=0
    for param in params:
        if index>0:
            addr+='&'+param
        else:
            addr+='?'+param
        index+=1
    result=requests.get(addr,headers=headers)
    return result

def diskSpace(diskPath):
    result=sendReq('diskspace')
    freeProc=0
    for disk in result.json():
        if disk['path'].find(diskPath)>=0:
            freeProc+=disk['freeSpace']*100/disk['totalSpace']
    return freeProc

def upcomingEp(days=1):
    listofep = []
    start = date.today().isoformat()
    end = (date.today()+timedelta(days=days)).isoformat()
    #print("From "+start+" to "+end)
    result=sendReq('calendar','start='+start,'end='+end)
    for data in result.json():
        seriesTitle = data['series']['title']
        seasonNum = data['seasonNumber']
        episodeNum = data['episodeNumber']
        airDate = (datetime.strptime(data['airDate'],'%Y-%m-%d')).date()
        deltaDays = airDate - date.today()
        #if delta.days >=0: print("+"+str(delta.days))
        #else: print(str(delta.days))
        #print(seriesTitle+' S'+str(seasonNum)+'E'+str(episodeNum))
        epInfo = {
                "seriesTitle":      seriesTitle,
                "seasonNumber":     seasonNum,
                "episodeNumber":    episodeNum,
                "airDate":          airDate,
                "deltaDays":        deltaDays,
                }
        listofep.append(epInfo)
    return listofep
