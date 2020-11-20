from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import json

accountID = "101-009-11751917-001"
access_token = '37277419e9d76f868cd3aef00ff49a95-ecf460f98e0f704098009ae5698a1017'

def Price():
        api = API(access_token=access_token, environment="practice")
        params = {
                "count": 6,
                "granularity": "H4"
                } 
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        return api.request(r)