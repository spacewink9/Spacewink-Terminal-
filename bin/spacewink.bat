@echo off
title Spacewink Terminal
cd /d "%~dp0"

echo Welcome to Spacewink Terminal!
echo.
echo Select an exchange to connect to:
echo 1. Binance
echo 2. Coinbase Pro
echo 3. Kraken
set /p exchange=Enter your choice: 

echo Select a market to trade:
echo 1. BTC-USDT
echo 2. ETH-USDT
echo 3. ADA-USDT
set /p market=Enter your choice: 

python main.py --exchange %exchange% --market %market%
