import datetime
import discord
import requests
import json
from bitflyer import public
import trade
import sys
import threading

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
    if message.content.startswith("-BTC"):
        p1 = public.Public().getticker()['best_bid']
        print(str(p1)+'円')
        await message.channel.send('> '+str(p1)+'円')

    if message.content.startswith("-ADK"):
        url = "https://aidosmarket.com/api/stats"
        r = requests.get(url).json()['stats']
        bid = r['bid']
        print(str(bid)+' BTC')
        await message.channel.send('> '+str(bid)+' BTC')

    if message.content.startswith("-USDJPY"):
        api = API(access_token=access_token, environment="practice")
        params = {
            "count": 6,
            "granularity": "H4"
            } 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        r = api.request(r)
        print(r['candles']['mid'])
        await message.channel.send(r)

    if message.content.startswith("-Rust"):
        await message.channel.send(trade.Price())

client.run(TOKEN) 