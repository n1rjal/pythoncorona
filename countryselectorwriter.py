import json
import pandas as pd
import os
import datetime

def scrapefile(filename):
    filename="./CSVs/"+filename
    countrydata=pd.read_csv(filename,index_col="Country")
    countries=['USA','Spain','Italy']
    
    tempdata={}
    
    for each in countries:
        tempdata[each]=list(countrydata.loc[each])
    #start of unpackng
    
    return(tempdata)    

cdata={}
files=os.listdir("./CSVs")
for eachfile in files:
    date=eachfile[4:14]
    cdata[date]=scrapefile(eachfile)


with open("./foredu/jsondata.json","w") as jsfile:
    json.dump(cdata,jsfile,indent=4)