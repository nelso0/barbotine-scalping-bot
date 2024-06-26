<p align="left">
  <img alt="Barbotine arbitrage bot Logo" width="10%" height="auto" src="https://i.ibb.co/gy9mb2k/logo.png">
</p>

[![Twitter @nelsorex](https://img.shields.io/twitter/url/https/twitter.com/nelsorex.svg?style=social&label=%20%40nelsorex)](https://twitter.com/nelsorex)
[![GitHub @nelso0](https://img.shields.io/github/followers/nelso0?label=follow&style=social)](https://github.com/nelso0)

⚠️ The code isn't in this repo, it's available for Capital supporters, more info [here](#full-version). ⚠️

Working on 10-second timeframe, Barbotine Scalping is a crypto scalping bot betting on the market manipulation happening on Bitfinex thanks to their detailed orderbook API. Included with the bot is a indicator I created for this purpose, the 'DWM', which means the bid/ask delta weighted-median BTC amount per user per order ratio.

## Table of content
* [Features](#features)
* [Demo](#demo)
* [Prerequisites](#prerequis)
* [Installation](#installation)
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

[video demo](https://www.youtube.com/watch?v=jj1aGm1p1fg)

The unavoidable question: is it profitable? To answer quickly, yes you can make money with it, and I made money with it. But this is speculation, so I'm not responsible of any kind of money you win or loose with my software, I'm a developer, not a fund manager.

<a name="prerequis"/>
 
## Prerequisites

The things you need before installing the software.

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

## Contact

Discord: nelsorex

Email: [nelso@barbotine.xyz](mailto:nelso@barbotine.xyz)

<a name="full-version"/>
 
## How do I  get it?

Source code available for Barbotine Capital supporters: [barbotine.xyz/](https://barbotine.xyz/)
