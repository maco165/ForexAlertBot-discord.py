import datetime
import discord
from discord.ext import tasks
import requests
import json
from bitflyer import public
import datetime
import time

from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

accountID = "101-009-11751917-001"
access_token = '37277419e9d76f868cd3aef00ff49a95-ecf460f98e0f704098009ae5698a1017'
TOKEN = 'NzQ5MTg1NTc2MTQ1NzgwNzk3.X0oTcA.MeiblwQQL1wZJah1cYIZ9BbSRF8' 
CHANNEL_ID = 668864142312210453
client =discord.Client()

def GetCandle(Count,Currncy):
    api = API(access_token=access_token, environment="practice")
    params = {"count":Count,"granularity":"H1"}
    r = instruments.InstrumentsCandles(instrument=Currncy, params=params)
    r = api.request(r)
    return r

def ReadyMessage(ftt,r,Currncy,embed):
    FTT= float(r.get('candles')[ftt]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
    if FTT<0:
        embed.add_field(name=Currncy,value='-----',inline=False)
        embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
        embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
        embed.add_field(name="FTT",value=':chart_with_downwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
        return embed
    else:
        embed.add_field(name=Currncy,value='-----',inline=False)
        embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
        embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
        embed.add_field(name="FTT",value=':chart_with_upwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
        return embed

@client.event
async def on_ready():
    while True:
        channel = client.get_channel(CHANNEL_ID)
        #
        #USDJPY
        r = GetCandle(8,"USD_JPY")
        embed = discord.Embed(title=":money_with_wings: Forex [JAPANTIME] Report :money_with_wings: ("+str(r.get('candles')[0]['time'].split('.')[0].split('T')[0])+')',color=0xff0000)
        Send = ReadyMessage(7,r,"USDJPY",embed) 
        #EURDJPY
        r = GetCandle(8,"EUR_JPY")
        Send = ReadyMessage(7,r,"EURJPY",embed) 
        #GBPJPY
        r = GetCandle(8,"GBP_JPY")
        Send = ReadyMessage(7,r,"GBPJPY",embed) 
        await channel.send(embed=Send)
        time.sleep(5)

client.run(TOKEN) 

'''


            api = API(access_token=access_token, environment="practice")
            params = {"count": 8,"granularity": "H1"} 
            r = instruments.InstrumentsCandles(instrument="GBP_JPY", params=params)
            r = api.request(r)
            FTT= float(r.get('candles')[7]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
            if FTT<0:
                embed.add_field(name="GBPJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
                embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
                embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
                embed.add_field(name="FTT",value=':chart_with_downwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
                await message.channel.send(embed=embed)
            else:
                embed.add_field(name="GBPJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
                embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
                embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
                embed.add_field(name="FTT",value=':chart_with_upwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
                await message.channel.send(embed=embed)


@tasks.loop(seconds=1)
async def loop():
    #USDJPY

    print(channel)
    
    await channel.send('1')

loop.start()
client.run(TOKEN) 

num = 0
for num in range(10):
    Date=list(r.get('candles')[num]["mid"])
    print(Date)

print(str(datetime.datetime.now()).split(' ')[1].split('.')[0].split(':')[1])
print('OPEN RATE '+str(r.get('candles')[0]["mid"]["o"]))
print('NOW RATE '+str(r.get('candles')[23]["mid"]["c"]))
FTT= float(r.get('candles')[23]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
if FTT<0:
    print('H1変動率 ' +'-'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ')
else:
    print('H1変動率 ' +'+'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ')
print(str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]))


while True:
    now=str(datetime.datetime.now()).split(' ')[1].split('.')[0]
    #JAPAN TIME
    if now == '17:00:00':
        api = API(access_token=access_token, environment="practice")
        params = {"count": 8,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        embed = discord.Embed(title="Forex RATE")
        embed.add_field(name="USDJPY")
        embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=False)
        embed.add_field(name="NOW RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=False)
        FTT= float(r.get('candles')[7]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
        if FTT<0:
            print('FTT ' +':chart_with_downwards_trend: '+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))
        else:
            print('FTT ' +':chart_with_upwards_trend:'+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'% ' + str(r.get('candles')[0]['time'].split('.')[0]))

    #LONDON TIME
    if now == '02:00:00':
        api = API(access_token=access_token, environment="practice")
        params = {"count": 10,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        print('OPEN RATE '+str(r.get('candles')[0]["mid"]["o"]))
        print('NOW RATE '+str(r.get('candles')[9]["mid"]["c"]))

    #NEW YORK TIME
    if now == '06:00:00':
        api = API(access_token=access_token, environment="practice")
        params = {"count": 9,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        print('OPEN RATE '+str(r.get('candles')[0]["mid"]["o"]))
        print('NOW RATE '+str(r.get('candles')[8]["mid"]["c"]))

    time.sleep(1)
'''