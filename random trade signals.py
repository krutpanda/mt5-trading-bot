import numpy as np
from krut.MetaTrader5 import *



def random(symbol):
    values = [True, False]
    buy = np.random.choice(values)
    sell = not buy
    return buy, sell

