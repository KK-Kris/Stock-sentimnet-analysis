from math import sqrt

# 引用词典
# Fuwei Jiang, Joshua Lee, Xiumin Martin, and Guofu Zhou.“Manager Sentiment and Stock Returns” Journal of Financial Economics 132(1), 2019,126-149
# 姜富伟、孟令超、唐国豪，“媒体文本情绪与股票回报预测”，《经济学(季刊)》，2021年第4期，第1323-1344页

import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import numpy as np

# from keras.losses import mean_absolute_error, mean_squared_error
# from sklearn.metrics import r2_score

df = pd.read_csv('688180comments.csv', encoding='gbk')  # header=0表示第一行是表头，就自动去除了
print(df)
title = df['title']
sentimentslist = []
for i in title:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

# with open('sentiment.csv', 'w', encoding='utf-8') as f:
#     for title in sentimentslist:
#         f.write(str(title)+"\n")
# f.close()


# df1 = pd.DataFrame([df['date'].index, sentimentslist], columns=['date', 'sentiment'])
# print(df1)
df['sentiment'] = sentimentslist
print(df)

# print(df_close)

dfJS = pd.read_csv('project_data/JunShi60test.csv', encoding='gbk')  # header=0表示第一行是表头，就自动去除了
print(dfJS)

df['date'] = [c.replace("-", "/") for c in df['date']]


def change_time_format(title_data):
    ##先弄后面 再弄前面
    transportation = []
    changedtimeformat = []
    for commenttime in title_data['date']:
        # print(commenttime)
        # print(commenttime[8])
        if commenttime[8] == "0":
            transportationtime = commenttime[:8] + commenttime[9:]
            # print(transportationtime)
            transportation.append(transportationtime)
        else:
            transportation.append(commenttime)
    for commenttime in transportation:
        # print(commenttime)
        # print(commenttime[5])
        if commenttime[5] == "0":
            changedtime = commenttime[:5] + commenttime[6:]
            # print(changedtime)
            changedtimeformat.append(changedtime)
        else:
            changedtimeformat.append(changedtime)
    # print(changedtimeformat)
    title_data['date'] = changedtimeformat

change_time_format(df)

print(df)
#
# outputpath='sentiment_data.csv'
# df.to_csv(outputpath, sep=',', index=False, header=False)

