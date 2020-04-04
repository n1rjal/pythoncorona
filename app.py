from plyer import notification
from tocsv import csv
import json
import datetime
import pandas as pd

todaydate=str(datetime.date.today())
todayfile="report {}.json".format(todaydate)
with open('./reports/{}'.format(todayfile),"r") as filee:
    datas=json.load(filee)

datafor=datas['nepal']
heads=(datas['head'])
print(heads)
msg=""
for i in range(1,6):
    msg=msg+str(heads[i]+ " : " +datafor[i]+"\n")

notification.notify(datafor[0].upper(),msg)