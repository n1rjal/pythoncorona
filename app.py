from plyer import notification
from tocsv import csv
import json
import datetime
import pandas as pd

def userdata(country):
    todaydate=str(datetime.date.today())
    todayfile="report {}.json".format(todaydate)
    print(todayfile+"\n")
    with open('./reports/{}'.format(todayfile),"r") as filee:
        datas=json.load(filee)
    datafor=datas[country]
    heads=(datas['head'])
    print(heads)
    msg=""
    for i in range(1,6):
        msg=msg+str(heads[i]+ " : " +datafor[i]+"\n")

    reply=(datafor[0].upper(),msg)
    return reply

def notify(title,body): 
    
    notification.notify(title,body)   
    