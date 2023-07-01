# this is a script with which you can check active positions and long & short quickly. For example, put in the terminal: "python a.py sell 0.001 BTC/USDT", and it will short 0.001 BTC/USDT. You can also check positions by putting "python a.py check BTC/USDT"

import ccxt.pro
from asyncio import run
import sys
from configuration import *

binance = getattr(ccxt.pro,'binanceusdm')({
            'apiKey':binance_usdm_futures_api_key,
            'secret':binance_usdm_futures_secret_key
        })

async def getp(symboli):
    global binance
    #lol2 = await binance.fetchBalance()
    lol2 = await binance.fetchPositions([symboli])
    #unrealizedPNL = lol2["unrealizedPnl"]
    #lol = await binance.createMarketSellOrder(symbol='BTC/USDT',amount=0.001)
    print(lol2)
    await binance.close()

async def trade(side,symboli,amounti):
    global binance
    #lol2 = await binance.fetchPositions([symboli])
    if side == "sell" or side == "buy":
        if side == "sell":
            lol = await binance.createMarketSellOrder(symbol=symboli,amount=amounti)
        if side == 'buy':
            lol = await binance.createMarketBuyOrder(symbol=symboli,amount=amounti)
    else:
        lol = "wrong command"
    
    print(lol)
    await binance.close()

if sys.argv[1] == 'sell':
    run(trade('sell',sys.argv[3],sys.argv[2]))
if sys.argv[1] == 'buy':
    run(trade('buy',sys.argv[3],sys.argv[2]))
if sys.argv[1] == 'check':
    run(getp(sys.argv[2]))