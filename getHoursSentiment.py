import pandas as pd
import matplotlib.pyplot as plt
from numpy import int16
from snownlp import SnowNLP
import numpy as np

# from keras.losses import mean_absolute_error, mean_squared_error
# from sklearn.metrics import r2_score

sentiment = pd.read_csv('sentiment_data.csv')
sentiment.columns = ['date', 'title', 'sentiment']
print(sentiment)

# print(sentiment['title'])

stockdata = pd.read_csv('688180stockdata.csv')
print(stockdata)

avg_sentiment = []
count = 0
for i in range(0, len(stockdata), 1):  ##
    # print(i)
    trade = stockdata['tradingtime'][i]
    stock_date = trade[:-6]
    stock_time = trade[-5:]
    print(stock_date)
    sentiment_1030 = 0
    number_1030 = 0
    sentiment_1130 = 0
    number_1130 = 0
    sentiment_1400 = 0
    number_1400 = 0
    sentiment_1500 = 0
    number_1500 = 0
    if stock_time == "10:30":
        for j in range(0, len(sentiment) - 1, 1):
            if sentiment['date'][j][:-5] == stock_date:
                sentiment_time = sentiment['date'][j][-4:]
                if 830 < int(sentiment_time) < 1030:
                    sentiment_1030 = sentiment_1030 + sentiment['sentiment'][j]
                    number_1030 = number_1030 + 1
    if stock_time == "11:30":
        for j in range(0, len(sentiment) - 1, 1):
            if sentiment['date'][j][:-5] == stock_date:
                sentiment_time = sentiment['date'][j][-4:]
                if 930 < int(sentiment_time) < 1130:
                    sentiment_1130 = sentiment_1130 + sentiment['sentiment'][j]
                    number_1130 = number_1130 + 1
    if stock_time == "14:00":
        for j in range(0, len(sentiment) - 1, 1):
            if sentiment['date'][j][:-5] == stock_date:
                sentiment_time = sentiment['date'][j][-4:]
                if 1200 < int(sentiment_time) < 1400:
                    sentiment_1400 = sentiment_1400 + sentiment['sentiment'][j]
                    number_1400 = number_1400 + 1
    if stock_time == "15:00":
        for j in range(0, len(sentiment) - 1, 1):
            if sentiment['date'][j][:-5] == stock_date:
                sentiment_time = sentiment['date'][j][-4:]
                if 1300 < int(sentiment_time) < 1500:
                    sentiment_1500 = sentiment_1500 + sentiment['sentiment'][j]
                    number_1500 = number_1500 + 1
    if stock_time == "10:30":
        if number_1030 > 0:
            sentiment_1030 = sentiment_1030 / number_1030
            avg_sentiment.append(sentiment_1030)
        if number_1030 == 0:
            avg_sentiment.append(0.5)
    if stock_time == "11:30":
        if number_1130 > 0:
            sentiment_1130 = sentiment_1130 / number_1130
            avg_sentiment.append(sentiment_1130)
        if number_1130 == 0:
            avg_sentiment.append(0.5)
    if stock_time == "14:00":
        if number_1400 > 0:
            sentiment_1400 = sentiment_1400 / number_1400
            avg_sentiment.append(sentiment_1400)
        if number_1400 == 0:
            avg_sentiment.append(0.5)
    if stock_time == "15:00":
        if number_1500 > 0:
            sentiment_1500 = sentiment_1500 / number_1500
            avg_sentiment.append(sentiment_1500)
        if number_1500 == 0:
            avg_sentiment.append(0.5)
    count = count + 1
    print(count)

print(avg_sentiment)
print(len(avg_sentiment))
stockdata['sentiment'] = avg_sentiment
print(stockdata)
outputpath ='stock_sentiment_data.csv'
stockdata.to_csv(outputpath, sep=',', index=False, header=False)
