<p align="left">
  <img alt="Barbotine Arbitrage System Logo" width="30%" height="30%" src="https://cdn.discordapp.com/attachments/876447732259225612/1095369391052443708/bas.svg">
</p>

[![Twitter @nelsodot](https://img.shields.io/twitter/url/https/twitter.com/nelsodot.svg?style=social&label=%20%40nelsodot)](https://twitter.com/nelsorex)
[![GitHub @nelso0](https://img.shields.io/github/followers/nelso0?label=follow&style=social)](https://github.com/nelso0)

Working on the BTC/USDT pair on 10-second timeframe, Barbotine Scalping is a crypto scalping bot betting on the market manipulation happening on Bitfinex thanks to their detailed orderbook API. Included with the bot is a indicator I created for this purpose, the 'DMW', which means the bid/ask delta weighted-median BTC amount per user per order ratio.

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
* True trading fees support
* Beginner-friendly functionning
* You can use the code for any other strategy, with permanent balance, trades and P&L displaying
* Trend-neutral
* User interface in terminal

<a name="demo"/>
 
## Demo

![ScalpingDemo1](https://media.discordapp.net/attachments/876447732259225612/1124293045987315712/scalping0.png)
![ScalpingDemo2](https://media.discordapp.net/attachments/876447732259225612/1124293046306099230/scalping1.png)
[video demo](https://www.youtube.com/watch?v=jj1aGm1p1fg)

The unavoidable question: is it profitable? To answer quickly, yes you can make money with it. But this is speculation, so I'm not responsible of any kind of money you win or loose with my software, I'm a developer, not a fund manager.

<a name="prerequis"/>
 
## Prerequisites

The things you need before installing the software.

* Only works with Binance USD-M Futures!
* Python 3.9+ (for windows users: if python or pip isn't recognized as a command, make sure you have installed python by checking the box "add to PATH")
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

It's all explained as clearly as I could on my website: https://barbotine.capital

## Contact

Discord: nelso#1800

Email: [nelso@barbotine.capital](mailto:nelso@barbotine.capital)

<a name="full-version"/>
 
## How do I  get it?

If you followed my precedent bot, Barbotine Arbitrage, you know that I've been working on this bot (and its strategy) for quite a long time. As the code's and strategy's quality is much much better than my precedent bot, I didn't know if I will share the source code publicly.

I finally decided to sell the source code publicly, so people can use it for their own things and learn.

Link to get the source code: [get.barbotine.capital](https://get.barbotine.capital/product/barbotine-scalping)
