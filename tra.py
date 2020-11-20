import datetime
import discord
import requests
import json
from bitflyer import public
import trade
import datetime

from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import json

accountID = "101-009-11751917-001"
access_token = '37277419e9d76f868cd3aef00ff49a95-ecf460f98e0f704098009ae5698a1017'
TOKEN = 'NzQ5MTg1NTc2MTQ1NzgwNzk3.X0oTcA.MeiblwQQL1wZJah1cYIZ9BbSRF8' 

print(str(datetime.datetime.now()).split(' ')[1].split('.')[0].split(':')[1])
api = API(access_token=access_token, environment="practice")
params = {"count": 24,"granularity": "H1"} 
r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
r = api.request(r)
print('OPEN RATE '+str(r.get('candles')[0]["mid"]["o"]))
print('NOW RATE '+str(r.get('candles')[23]["mid"]["c"]))
FTT= float(r.get('candles')[23]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
if FTT<0:
    print('H1変動率 ' +'-'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ')
else:
    print('H1変動率 ' +'+'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ')



'''
while True:
    now=str(datetime.datetime.now()).split(' ')[1].split('.')[0]

    #JAPAN TIME
    if now == '17:00:00':
        api = API(access_token=access_token, environment="practice")
        params = {"count": 8,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        print('NOW RATE '+str(r.get('candles')[7]["mid"]["c"]))
        FTT= float(r.get('candles')[7]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])

    #LONDON TIME
    if now == '02:00:00':
        api = API(access_token=access_token, environment="practice")
        params = {"count": 10,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        print('NOW RATE '+str(r.get('candles')[9]["mid"]["c"]))

    #NEW YORK TIME
    if now == '06:00:00':
        api = API(access_token=access_token, environment="practice")
        params = {"count": 9,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        print('NOW RATE '+str(r.get('candles')[8]["mid"]["c"]))
'''

#H1
api = API(access_token=access_token, environment="practice")
params = {
          "count": 1,
          "granularity": "H1"
         } 
r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
r = api.request(r)
print('NOW RATE '+str(r.get('candles')[0]["mid"]["o"]))
FTT= float(r.get('candles')[0]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
if FTT<0:
    print('H1 変動率 ' +'-'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))
else:
    print('H1 変動率 ' +'+'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))

#H4
params = {
          "count": 1,
          "granularity": "H4"
         } 
r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
r = api.request(r)
FTT= float(r.get('candles')[0]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
if FTT<0:
    print('H4 変動率 ' +'-'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))
else:
    print('H4 変動率 ' +'+'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))

#D1
params = {
          "count": 1,
          "granularity": "D"
         } 
r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
r = api.request(r)
FTT= float(r.get('candles')[0]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
if FTT<0:
    print('D1 変動率 ' +'-'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))
else:
    print('D1 変動率 ' +'+'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))