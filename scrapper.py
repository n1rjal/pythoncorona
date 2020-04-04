from bs4 import BeautifulSoup
import requests
import json
import datetime

url="https://www.worldometers.info/coronavirus/"
sauce=requests.get(url).content
soup=BeautifulSoup(sauce,"html.parser")
table=soup.findAll("div",class_="tab-content")
tablediv=table[2]
table=tablediv.find("table",class_="table table-bordered table-hover main_table_countries")

thead=table.find("thead")
tr=thead.find("tr")
th=tr.findAll("th")

heads=[]
for h in th:
    heads.append(h.text)

tbody=table.find("tbody")



datas={}
datas['head']=heads
listoftr=tbody.findAll("tr")
for tr in listoftr:
    key=""
    data=[]
    tds=tr.findAll("td")        
    key=tds[0].text
    for dat in tds:
        data.append((dat.text).replace(",",""))
    datas[key.lower()]=data

filename='report '+str(datetime.date.today())+'.json'

filee=open("./reports/"+filename,'w')
json.dump(datas,filee)
filee.close()