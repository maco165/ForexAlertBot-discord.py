import discord
from discord.ext import tasks
from datetime import datetime 
import time
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

TOKEN = 'NzQ5MTg1NTc2MTQ1NzgwNzk3.X0oTcA.MeiblwQQL1wZJah1cYIZ9BbSRF8' 
CHANNEL_ID =668864142312210453
accountID = "101-009-11751917-001"
access_token = '37277419e9d76f868cd3aef00ff49a95-ecf460f98e0f704098009ae5698a1017'


client = discord.Client()

@client.event
async def on_ready():
  while True:
    channel = client.get_channel(CHANNEL_ID)
    api = API(access_token=access_token, environment="practice")
    params = {"count": 8,"granularity": "H1"} 
    r = instruments.InstrumentsCandles(instrument="GBP_JPY", params=params)
    r = api.request(r)
    FTT= float(r.get('candles')[7]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
    if FTT<0:
      embed = discord.Embed(title=" Forex Report ",color=0xff0000)
      embed.add_field(name="GBPJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
      embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
      embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
      embed.add_field(name="FTT",value=':chart_with_downwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
      await channel.send(embed=embed)
    else:
      embed = discord.Embed(title=" Forex Report ",color=0xff0000)
      embed.add_field(name="GBPJPY",value=str(r.get('candles')[0]['time'].split('.')[0].split('T')[0]),inline=False)
      embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
      embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
      embed.add_field(name="FTT",value=':chart_with_upwards_trend:'+str(round(FTT,2)*10)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
      await channel.send(embed=embed)

    time.sleep(5)

client.run(TOKEN)