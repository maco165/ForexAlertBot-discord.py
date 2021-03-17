import time
import datetime
import discord
import pytz
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import pandas as pd
import mplfinance as mpf

accountID = " "
access_token = ' '
TOKEN = ' ' 
CHANNEL_ID = 
client =discord.Client()

def GetCandle(Count,Currncy,CandleTime):
    api = API(access_token=access_token, environment="practice")
    params = {"count":Count,"granularity":CandleTime}
    r = instruments.InstrumentsCandles(instrument=Currncy, params=params)
    r = api.request(r)
    return r
def ReadyMessage(ftt,r,Currncy,embed):
    FTT= float(r.get('candles')[ftt]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
    if FTT<0:
        embed.add_field(name=Currncy,value='-----',inline=False)
        embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
        embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
        embed.add_field(name="FTT",value=':chart_with_downwards_trend:'+str(round(FTT,2)*100)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
        return embed
    else:
        embed.add_field(name=Currncy,value='-----',inline=False)
        embed.add_field(name="OPEN RATE",value=str(r.get('candles')[0]["mid"]["o"]),inline=True)
        embed.add_field(name="CLOSE RATE",value=str(r.get('candles')[7]["mid"]["c"]),inline=True)
        embed.add_field(name="FTT",value=':chart_with_upwards_trend:'+str(round(FTT,2)*100)+ 'Pips ('+ str(round((abs(FTT)/float(r.get('candles')[0]["mid"]["o"])*100),2))+'%)')
        return embed
def VolAlert(r,Now,Currncy):
    FTT= float(r.get('candles')[14]["mid"]["c"])-float(r.get('candles')[0]["mid"]["o"])
    if round(abs(FTT),2)*100>10:
        if FTT<0:
            embed = discord.Embed(title="PRICE ALERT ("+Now+')')
            embed.add_field(name=Currncy,value=':chart_with_downwards_trend:'+str(round(abs(FTT),2)*100)+' Pips',inline=False)
            return embed
        else:
            embed = discord.Embed(title="PRICE ALERT ("+Now+')')
            embed.add_field(name=Currncy,value=':chart_with_upwards_trend:'+str(round(abs(FTT),2)*100)+' Pips',inline=False)
            return embed
    else:
        return 0
def ImageGene(Currncy,CandleTime,Count):
    r = GetCandle(Count,Currncy,CandleTime)
    df = pd.DataFrame({'open': [], 'high': [], 'low': [],'close': []},index=[])
    for i in range(Count-1):
        df.loc[pd.to_datetime(r.get('candles')[i]["time"].split('.')[0].split('T')[1])] = [float(r.get('candles')[i]["mid"]["o"]),float(r.get('candles')[i]["mid"]["h"]),float(r.get('candles')[i]["mid"]["l"]),float(r.get('candles')[i]["mid"]["c"])]
    mpf.plot(df,type='candle',savefig='candlestick_mpf.png')
    return 0

@client.event
async def on_ready():
    counter = 0
    while True:
        Now=str(datetime.datetime.now(pytz.timezone('Asia/Tokyo'))).split(' ')[1].split('.')[0]
        Theweek = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        channel = client.get_channel(CHANNEL_ID)
        if Theweek.strftime('%a') == 'Sat' or Theweek.strftime('%a') == 'Sun':
            pass
        else:
            #変動アラート
            if counter >0:
                counter -= 1
            if counter == 0:
                r = GetCandle(15,"USD_JPY","M1")
                embed = VolAlert(r,Now,'USDJPY')
                if embed == 0:
                    pass 
                else:
                    embed.set_thumbnail(url="https://moneymunch.com/wp-content/uploads/2016/09/01-USD-JPY.png")
                    await channel.send(embed=embed)
                    image = ImageGene("USD_JPY",'M1',100)
                    await channel.send("USDJPY")
                    await channel.send(file=discord.File('candlestick_mpf.png'))
                    counter=900
                r = GetCandle(15,"EUR_JPY","M1")
                embed = VolAlert(r,Now,'EURJPY')
                if embed == 0:
                    pass 
                else:
                    embed.set_thumbnail(url="https://i-invdn-com.akamaized.net/news/EUR-JPY_2_800x533_L_1417097360.jpg")
                    await channel.send(embed=embed)
                    image = ImageGene("EUR_JPY",'M1',100)
                    await channel.send("EURJPY")
                    await channel.send(file=discord.File('candlestick_mpf.png'))
                    counter=900
                r = GetCandle(15,"GBP_JPY","M1")
                embed = VolAlert(r,Now,'GBPJPY')
                if embed == 0:
                    pass 
                else:
                    embed.set_thumbnail(url="https://i-invdn-com.akamaized.net/news/GBP-JPY_2_800x533_L_1417097677.jpg")
                    await channel.send(embed=embed)
                    image = ImageGene("GBP_JPY",'M1',100)
                    await channel.send("GBPJPY")
                    await channel.send(file=discord.File('candlestick_mpf.png'))
                    counter=900

            #定期アラート
            #JAPANTIME
            if Now == '17:00:00':
                r = GetCandle(8,"USD_JPY","H1")
                embed = discord.Embed(title=":money_with_wings: Forex [JAPAN TIME] Report :money_with_wings: ("+str(r.get('candles')[0]['time'].split('.')[0].split('T')[0])+')',color=0xff0000)
                Send = ReadyMessage(7,r,"USDJPY",embed) 
                r = GetCandle(8,"EUR_JPY","H1")
                Send = ReadyMessage(7,r,"EURJPY",embed) 
                r = GetCandle(8,"GBP_JPY","H1")
                Send = ReadyMessage(7,r,"GBPJPY",embed) 
                await channel.send(embed=Send)
                image = ImageGene("USD_JPY",'M10',48)
                await channel.send("USDJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
                image = ImageGene("EUR_JPY",'M10',48)
                await channel.send("EURJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
                image = ImageGene("GBP_JPY",'M10',48)
                await channel.send("GBPJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
            #LONDON TIME
            if Now == '02:00:00':
                r = GetCandle(10,"USD_JPY","H1")
                embed = discord.Embed(title=":money_with_wings: Forex [LONDON TIME] Report :money_with_wings: ("+str(r.get('candles')[0]['time'].split('.')[0].split('T')[0])+')',color=0xff0000)
                Send = ReadyMessage(9,r,"USDJPY",embed) 
                r = GetCandle(10,"EUR_JPY","H1")
                Send = ReadyMessage(9,r,"EURJPY",embed) 
                r = GetCandle(10,"GBP_JPY","H1")
                Send = ReadyMessage(9,r,"GBPJPY",embed) 
                await channel.send(embed=Send)
                image = ImageGene("USD_JPY",'M10',60)
                await channel.send("USDJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
                image = ImageGene("EUR_JPY",'M10',60)
                await channel.send("EURJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
                image = ImageGene("GBP_JPY",'M10',60)
                await channel.send("GBPJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
            #NEW YORK TIME
            if Now == '06:00:00':
                r = GetCandle(9,"USD_JPY","H1")
                embed = discord.Embed(title=":money_with_wings: Forex [NEWYORK TIME] Report :money_with_wings: ("+str(r.get('candles')[0]['time'].split('.')[0].split('T')[0])+')',color=0xff0000)
                Send = ReadyMessage(8,r,"USDJPY",embed) 
                r = GetCandle(9,"EUR_JPY","H1")
                Send = ReadyMessage(8,r,"EURJPY",embed) 
                r = GetCandle(9,"GBP_JPY","H1")
                Send = ReadyMessage(8,r,"GBPJPY",embed) 
                await channel.send(embed=Send)
                image = ImageGene("USD_JPY",'M10',54)
                await channel.send("USDJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
                image = ImageGene("EUR_JPY",'M10',54)
                await channel.send("EURJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
                image = ImageGene("GBP_JPY",'M10',54)
                await channel.send("GBPJPY")
                await channel.send(file=discord.File('candlestick_mpf.png'))
        time.sleep(1)
client.run(TOKEN) 
