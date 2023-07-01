import ccxt.pro
from asyncio import run
import sys
from os import name,system
import asyncio
from colorama import * 
from datetime import datetime
import statistics
import weightedstats as ws

def write_and_delete(file_name, text_to_append):
    with open(file_name, 'w') as file_object:
        file_object.write(text_to_append)
        file_object.close()
def append_new_line(file_name, text_to_append):
    with open(file_name, 'a+') as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write('\n')
        file_object.write(text_to_append)
def clear():

    if name == 'nt':
      system('cls')
    else:
        system('clear')

delta_weighted_median_amount_per_user_pct_list = []
price_list = []

symbol='BTC/USD'

clear()
print(f"""
   ___    ___    ___    ___   ____  ______   ____   _  __   ____
  / _ )  / _ |  / _ \  / _ ) / __ \/_  __/  /  _/  / |/ /  / __/
 / _  | / __ | / , _/ / _  |/ /_/ / / /    _/ /   /    /  / _/  
/_____//_/ |_|/_/|_| /____/ \____/ /_/    /___/  /_/|_/  /___/  
   ____  _____   ___    __    ___    ____   _  __  _____        
  / __/ / ___/  / _ |  / /   / _ \  /  _/  / |/ / / ___/        
 _\ \  / /__   / __ | / /__ / ___/ _/ /   /    / / (_ /         
/___/  \___/  /_/ |_|/____//_/    /___/  /_/|_/  \___/          
                                                                \n \nby @nelsorex""")
print(f" \n{Fore.YELLOW}{Style.BRIGHT}BACKTESTING DATA COLLECTOR{Style.RESET_ALL}\n \n")

async def main():
    global balances,symbol,delta_volume_binance_list
    binanceasync = getattr(ccxt.pro,'binanceusdm')()
    exchange = getattr(ccxt.pro,'bitfinex')()
    asset = symbol.split('/', 1)[0]
    i=0

    while True:
        i=1
        while True:
            orderbook = await exchange.watch_order_book(symbol)
            orderbookbinance = await binanceasync.watch_order_book('BTC/USDT')
            price = orderbookbinance['asks'][0][0]
            bid_amounts = [bid[1] for bid in orderbook['bids']]
            ask_amounts = [ask[1] for ask in orderbook['asks']]
            bid_user_counts = [bid[2] for bid in orderbook['bids']]
            ask_user_counts = [ask[2] for ask in orderbook['asks']]

            if sum(bid_user_counts) == 0 or sum(ask_user_counts) == 0:
                break
            avg_bid_amount_per_user = sum(bid_amounts) / sum(bid_user_counts)
            avg_ask_amount_per_user = sum(ask_amounts) / sum(ask_user_counts)
            delta_bid_ask = avg_bid_amount_per_user - avg_ask_amount_per_user
            delta_bid_ask_pct = (delta_bid_ask/(avg_bid_amount_per_user+avg_ask_amount_per_user)/2)*100

            median_bid_amount_per_user = statistics.median(bid_amounts)
            median_ask_amount_per_user = statistics.median(ask_amounts)

            delta_median_amount_per_user = median_bid_amount_per_user-median_ask_amount_per_user
            delta_median_amount_per_user_pct = delta_median_amount_per_user/((median_bid_amount_per_user+median_ask_amount_per_user)/2)

            weighted_median_bid_amount_per_user = ws.weighted_median(bid_amounts,bid_user_counts)
            weighted_median_ask_amount_per_user = ws.weighted_median(ask_amounts,ask_user_counts)

            delta_weighted_median_amount_per_user = weighted_median_bid_amount_per_user-weighted_median_ask_amount_per_user
            delta_weighted_median_amount_per_user_pct = delta_weighted_median_amount_per_user/((weighted_median_bid_amount_per_user+weighted_median_ask_amount_per_user)/2)

            delta_weighted_median_amount_per_user_pct_list.append(delta_weighted_median_amount_per_user_pct)
            price_list.append(price)

            #binance_spread_list.append(binance_spread)
            #bitfinex_spread_list.append(bitfinex_spread)

            write_and_delete(f"dmw.txt",f"{str(delta_weighted_median_amount_per_user_pct_list)}")
            write_and_delete(f"price.txt",f"{str(price_list)}")

            print(f"DWM: {round(delta_weighted_median_amount_per_user_pct,3)}")
            print(f"PRICE: {round(price,3)}")
            print(f" ")
            print(f"Number of hours recorded: {round((i*10)/60/60,2)}")

            for i in range(4):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")

            await asyncio.sleep(10)
            i+=1

            

run(main())