import json
import urllib.request
from Database import*

"""
Finished: 8/27/2020

listtostringforjson() takes a list, in this case from database.py and turns it into a string adding a ',' between each 
item

writedata() uses the Albion Online api to pull real time data from the in game economy and market in the form of a json 
and writes it to a local jsonfile called data.json

example of a single item pulled from the game api:
{"item_id": "T3_PLANKS", "city": "Black Market", "quality": 1, "sell_price_min": 0, "sell_price_min_date": "0001-01-01T00:00:00", 
 "sell_price_max": 0, "sell_price_max_date": "0001-01-01T00:00:00", "buy_price_min": 0, "buy_price_min_date": "0001-01-01T00:00:00", 
 "buy_price_max": 0, "buy_price_max_date": "0001-01-01T00:00:00"}
 
we will iterate through a list with different "item_id" and "city" types/strings to get all of the data that we want 

*important: found out that when we call the game api if we leave the city catagory blank, it will automatically give us 
a json with all the cities in it
"""

def listToStringForJson(l):
    bob = ''
    for x in l:
        bob+= str(x)+','

    return bob


def writeData(l):
    pricedata = json.load(urllib.request.urlopen("https://www.albion-online-data.com/api/v2/stats/prices/" + listToStringForJson(l) + "?locations&qualities=1"))
    with open('data.json', 'w') as j:
        json.dump(pricedata, j)



