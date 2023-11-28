<p align="left">
  <img alt="Barbotine Arbitrage System Logo" width="30%" height="30%" src="https://cdn.discordapp.com/attachments/876447732259225612/1095369391052443708/bas.svg">
</p>

[![Twitter @nelsodot](https://img.shields.io/twitter/url/https/twitter.com/nelsodot.svg?style=social&label=%20%40nelsodot)](https://twitter.com/nelsorex)
[![GitHub @nelso0](https://img.shields.io/github/followers/nelso0?label=follow&style=social)](https://github.com/nelso0)

⚠️ The code isn't in this repo, I made it private, more info [here](#full-version). ⚠️

Working on 10-second timeframe, Barbotine Scalping is a crypto scalping bot betting on the market manipulation happening on Bitfinex thanks to their detailed orderbook API. Included with the bot is a indicator I created for this purpose, the 'DWM', which means the bid/ask delta weighted-median BTC amount per user per order ratio.

## Table of content
* [Features](#features)
* [Demo](#demo)
* [Prerequisites](#prerequis)
* [Installation](#installation)
* [How does it work](#howwork)
* [Contact](#contact)
* [How do I get it?](#full-version)
<a name="features"/>
 
## Features

* All settings are editable (leverage, stop-loss...)
* True trading fees offline support
* Not based on technical indicators bullshit, only on orderbook moves, price action and market manipulation
* Backtests + data collecting script
* Trend-neutral
* User interface in terminal

<a name="demo"/>
 
## Demo

![ScalpingDemo1](https://media.discordapp.net/attachments/876447732259225612/1124293045987315712/scalping0.png)
![ScalpingDemo2](https://media.discordapp.net/attachments/876447732259225612/1124293046306099230/scalping1.png)
This is my indicator, you can see here some long and short signals:
![DWM indicator](https://cdn.discordapp.com/attachments/876447732259225612/1133362934832185344/IMG_2034.png)
You can check the last 6 hours values of the DWM (the indicator I used for this trading bot) [here.](https://barbotine.capital/dwm)


[video demo](https://www.youtube.com/watch?v=jj1aGm1p1fg)

The unavoidable question: is it profitable? To answer quickly, yes you can make money with it, and I made money with it. But this is speculation, so I'm not responsible of any kind of money you win or loose with my software, I'm a developer, not a fund manager.

<a name="prerequis"/>
 
## Prerequisites

The things you need before installing the software.

* Only compatible with Binance USD-M futures, Kucoin futures and Poloniex futures for now!
* Python 3.9+
* Nothing else lol

<a name="installation"/>
 
## Installation (when you have the source code)

1. Install all the requirements to run the scalping bot
```sh
pip install -r requirements.txt
```
2. Set your configuration details in [configuration.py](configuration.py)
3. Run with:
```sh
python bot.py
```

<a name="howwork"/>
 
## How does it work?

It's all explained on my website: [https://barbotine.capital](https://barbotine.capital/scalping)

## Contact

Discord: nelsorex

Email: [nelso@barbotine.capital](mailto:nelso@barbotine.capital)

<a name="full-version"/>
 
## How do I  get it?

The source code is now available for purchase: [barbotine.capital/scalping](https://barbotine.capital/pricing)
