import datetime
import discord
import requests
import json
from bitflyer import public
import trade
import sys
import threading
import time

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
client =discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("-JAPANTIME"):
        #USDJPY
        api = API(access_token=access_token, environment="practice")
        params = {"count": 8,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        FTT= float(r.get('candles')[7]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
        if FTT<0:
            embed = discord.Embed(title="Forex RATE",color=0xff0000)
            embed.add_field(name="USDJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
            embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
            embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
            embed.add_field(name="FTT",value=':chart_with_downwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
        else:
            embed = discord.Embed(title="Forex RATE",color=0xff0000)
            embed.add_field(name="USDJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
            embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
            embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
            embed.add_field(name="FTT",value=':chart_with_upwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')

        #EURJPY
        api = API(access_token=access_token, environment="practice")
        params = {"count": 8,"granularity": "H1"} 
        r = instruments.InstrumentsCandles(instrument="EUR_JPY", params=params)
        r = api.request(r)
        FTT= float(r.get('candles')[7]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
        if FTT<0:
            embed.add_field(name="EURJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
            embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
            embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
            embed.add_field(name="FTT",value=':chart_with_downwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
        else:
            embed.add_field(name="EURJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
            embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
            embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
            embed.add_field(name="FTT",value=':chart_with_upwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')

        #GBPJPY
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

client.run(TOKEN) 