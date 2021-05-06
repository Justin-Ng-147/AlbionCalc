import json
import urllib.request
import datetime
from Database import*

"""
date: 8/27/2020

IMPORTANT: This file is no longer being used in the actual project. It is only kept here for my learning experience
and as a reference to look back on

This file was used initially before I made the decision to use google sheets to display all of my data
If I had not made that decision this is what it would have looked like: 

T5_WOOD_LEVEL3@3 | 12900 | 2020-08-27T06:15:00 | FortSterling
T5_WOOD_LEVEL3@3 | 7501 | 2020-08-03T00:00:00 | Thetford
T5_WOOD_LEVEL3@3 | 9981 | 2020-08-26T21:45:00 | Martlock
T5_WOOD_LEVEL3@3 | 7020 | 2020-08-03T12:00:00 | Bridgewatch
T5_WOOD_LEVEL3@3 | 11996 | 2020-08-27T01:15:00 | Lymhurst
T5_WOOD_LEVEL3@3 | 6000 | 2020-08-26T20:50:00 | Carleon

originally this project was going to be used do many calculations using the in game data ex. profits made from doing
this action, price predictions, crafting recipe calculations, side by side price graphing, etc
but I have found out that someone already made it easier to do these calculations and all that I need to do was the 
data needed 
"""

class Plank:
    def __init__(self, name, city, price, age):
        self.price = price
        self.age = age
        self.name = name
        self.city = city
        #timeDif = datetime.datetime.utcnow()-age

class HolyStaffs:
    def __init__(self, name, city, price, age):
        self.name = name
        self.city = city
        self.price = price
        self.age =age
        input1 = 12
        input2 = 6

class LeatherHelm:
    def __init__(self,name,city,price,age,arti):
        self.name = name
        self.city = city
        self.price = price
        self.age = age
        self.arti = arti
        input = 8

def getPlankPrice(id, city):
    pricedata = json.load(urllib.request.urlopen("https://www.albion-online-data.com/api/v2/stats/prices/"+id+"?locations="+city+"&qualities=1"))
    return Plank(id, city, pricedata[0]['sell_price_min'], pricedata[0]['sell_price_min_date'])

def getPlankPriceArray(id):
    Planks = []
    for x in CityIds:
        Planks.append(getPlankPrice(id, x))
    return Planks

print(datetime.datetime.utcnow())

def main():
    for x in LogIds:
        for y in getPlankPriceArray(x):
            printValues = (str(y.name)+" | "+str(y.price)+" | "+str(y.age)+" | "+str(y.city))
            print(printValues)

main()