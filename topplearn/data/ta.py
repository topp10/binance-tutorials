import numpy
import talib

my_data = numpy.genfromtxt('topplearn/data/2020-2021-5M.csv', delimiter=',')

# print(my_data)

close = my_data[:,4]

# print(close)

# close = numpy.random.random(100)

# # print(close)

# moving_average = talib.SMA(close, timeperiod=10)

# print(moving_average)

rsi = talib.RSI(close)

print(rsi)