import config1, csv
from binance.client import Client

client = Client(config1.API_KEY, config1.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#     print(prices)

# candles = client.get_historical_klines(symbol='BTCUSDT', interval=client.KLINE_INTERVAL_15MINUTE, start_str=1615507200000)

csvfile = open('topplearn/data/2020-2021-5M.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# for candlestick in candles:
#     print(candlestick)

#     candlestick_writer.writerow(candlestick)

# print(len(candles))

candlesticks = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_5MINUTE, start_str="1 Jan, 2020")

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close()