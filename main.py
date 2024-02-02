import MetaTrader5 as mt5
import pandas as pd
import numpy as np

import time
from KRUTPANDA.MetaTrader5 import *
from datetime import datetime, timedelta
from KRUTPANDA.LiveTradingSignal import *
import warnings
warnings.filterwarnings("ignore")

symbol = "EURUSD"
lot = 0.01
magic = 06052003
timeframe = timeframes_mapping["1-minute"]
pct_tp, pct_sl = 0.005, 0.005 # DO NOT PUT __*****THE MINUS SYMBOL*****__ ON THE SL
mt5.initialize()

current_account_info = mt5.account_info()
print("------------------------------------------------------------------")
print(f"Login: {mt5.account_info(123419111).login} \tserver: {mt5.account_info(Exness-MT5Trial7).server}")
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(
    f"Balance: {current_account_info.balance} USD, \t Equity: {current_account_info.equity} USD, \t Profit: {current_account_info.profit} USD")
print("------------------------------------------------------------------")

timeframe_condition = get_verification_time(timeframe[1])

while True:

    if datetime.now().strftime("%H:%M:%S") in timeframe_condition:
        print(datetime.now().strftime("%H:%M:%S"))

        # ! in market watch you have to selecte pair if you have to open or close the oder
        selected = mt5.symbol_select(symbol)
        if not selected:
            print(f"\nERROR - mitra error  '{symbol}' in MetaTrader 5 with error :", mt5.last_error())

        # Create signals if you have to gain profit$$$$
        buy, sell = random(symbol)

        # Import @@live@@ open positions
        res = resume()

        # Here we have a tp-sl signal, and we can't open two position on the same asset for the same strategy
        if ("symbol" in res.columns) and ("volume" in res.columns):
            if not ((res["symbol"] == symbol) & (res["volume"] == lot)).any():
                # Run the algorithm
                run(symbol, buy, sell, lot, pct_tp=pct_tp, pct_sl=pct_sl, magic=magic)

        else:
            run(symbol, buy, sell, lot, pct_tp=pct_tp, pct_sl=pct_sl, magic=magic)
    
        time.sleep(1)
