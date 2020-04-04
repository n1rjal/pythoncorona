from scrapper import exec

import pandas as pd
import json
import os
import datetime


def csv():

    date=str(datetime.date.today())
    filename='report '+date+'.json'
    files=os.listdir('./reports')
    if filename in files:
        #lets read from the data of json file
        with open('./reports/{}'.format(filename),'r') as filee:
            datas=json.load(filee)
    else:
        exec()
        print("Using a new data for today")
        with open('./reports/{}'.format(filename),'r') as filee:
            datas=json.load(filee)




    #making empty lists
    countries=[]
    totalcases=[]
    newcases=[]
    totaldeaths=[]
    newdeaths=[]
    totalrecovered=[]
    activecases=[]
    serious=[]
    critical=[]
    totaltest=[]

    #for viewing the data we need to
    #delete the head part
    datas.pop("head")

    #indexing as the value goes
    for countrykey, data in datas.items():
        countries.append(data[0])
        totalcases.append(data[1])
        newcases.append(data[2])
        totaldeaths.append(data[3])
        newdeaths.append(data[4])
        totalrecovered.append(data[5])
        activecases.append(data[6])
        serious.append(data[7])
        critical.append(data[8])
        totaltest.append(data[11])
        
    csvdata=pd.DataFrame({
        "Country":countries,
        "Total Cases":totalcases,
        "New Cases":newcases,
        "Total Deaths":totaldeaths,
        "New Deaths":newdeaths,
        "Total Recovered":totalrecovered,
        "Active Cases":activecases,
        "Serious Cases":serious,
        "Critical Cases":critical,
        "Total Test":totaltest
    })


    #use this command to get data in csv
    csvdata.to_csv("coronadata.csv")
    print("done")