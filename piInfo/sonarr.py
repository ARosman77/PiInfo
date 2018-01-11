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
    """ Send request to API with headers and parameters """
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
    """ Return procentage of freespace on disk mounted at diskPath """
    result=sendReq('diskspace')
    freeProc=0
    for disk in result.json():
        if disk['path'].find(diskPath)>=0:
            freeProc+=disk['freeSpace']*100/disk['totalSpace']
    return freeProc

def upcomingEp(days=1):
    """ Return list of upcoming episodes """
    listofep = []
    start = date.today().isoformat()
    end = (date.today()+timedelta(days=days)).isoformat()
    result=sendReq('calendar','start='+start,'end='+end)
    for data in result.json():
        seriesTitle = data['series']['title']
        seasonNum = data['seasonNumber']
        episodeNum = data['episodeNumber']
        airDate = (datetime.strptime(data['airDate'],'%Y-%m-%d')).date()
        deltaDays = airDate - date.today()
        # new info added for Issue #7
        bHasFile = data['hasFile']
        seriesId = data['seriesId']
        epId = data['id'] 
        epInfo = {
                "seriesTitle":      seriesTitle,
                "seasonNumber":     seasonNum,
                "episodeNumber":    episodeNum,
                "airDate":          airDate,
                "deltaDays":        deltaDays,
                "hasFile":          bHasFile,
                "seriesId":         seriesId,
                "epid":             epId,
                }
        listofep.append(epInfo)
    return listofep

def queueInfo():
    """ Return download queue content """
    info = []
    result=sendReq('queue')
    if len(result.json()) <= 0:
        # return [{}] # what to return
        return info
    for data in result.json():
        epId = data['episode']['id']
        size = data['size']
        sizeleft = data['sizeleft']
        prDone = sizeleft/size*100
        qinfo = {
                "epId":         epId,
                "size":         size,
                "sizeleft":     sizeleft,
                "prDone":       prDone,
                }
        info.append(qinfo)
    return info

def isInQueue(episodeId):
    """ Return true if episode is in download queue """
    qInfo = queueInfo()
    for ep in qInfo:
        if ep["epId"] == episodeId:
            return 1
