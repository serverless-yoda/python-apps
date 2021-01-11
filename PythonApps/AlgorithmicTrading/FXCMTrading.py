import fxcmpy
import os
import pandas as pd
import time

#get script filename location
absFilePath = os.path.abspath(__file__)

#get folder of the dictionary
path, filename = os.path.split(absFilePath)
#print("Script file path is {}, filename is {}".format(path, filename))

dictionaryPath = path + "\\FXCM.cfg"
print(dictionaryPath)

#open the connections
api = fxcmpy.fxcmpy(config_file= dictionaryPath)


#print(api.get_accounts())
print("*" * 40)
print("Account Number:{}".format(api.get_account_ids()[0]))
print("Currency Traded:{}".format(api.get_instruments()[0]))
print("*" * 40)

print("HISTORICAL DATE")
#get historical date
#period can be H1,D1,m1
df1 = api.get_candles("EUR/USD", number = 5,columns=["bids"], start = "2020-07-01", end = "2020-07-31", period="H1")
#df2 = api.get_candles("EUR/USD", number = 5,columns=["asks"])

#df.info()
print(df1)

print("REAL TIME DATA")
api.subscribe_market_data("EUR/USD")
api.get_subscribed_symbols()
print(api.get_last_price("EUR/USD"))
print(api.get_prices("EUR/USD"))

while True:
    time.sleep(1)
    print(api.get_last_price("EUR/USD").name,api.get_last_price("EUR/USD").Bid,api.get_last_price("EUR/USD").Ask, sep ="|")