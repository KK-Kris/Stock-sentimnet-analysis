# 读取数据
from math import sqrt

import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import LSTM, Dropout, Dense
# from keras.losses import mean_squared_error, mean_absolute_error
from keras.losses import mean_squared_error, mean_absolute_error
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

##把stock_sentiment_data中的close和sentiment交换一下
from sklearn.svm import SVR

stockdatawithsentiment = pd.read_csv('+-stock_sentiment_data.csv', index_col='date')
stockdatawithsentiment['volume'] = [int(c.replace(",", "")) for c in stockdatawithsentiment['volume']]
# print(stockdatawithsentiment)

standard = MinMaxScaler()
standard = standard.fit(stockdatawithsentiment)
normaldata = standard.fit_transform(stockdatawithsentiment)
print(normaldata[:5, :])
# 打印前5行

# 将ndarray的dtype为float32，防止报错
normaldata = normaldata.astype(np.float32)
# 训练集:验证集=7:3
X_train, X_test, Y_train, Y_test = train_test_split(normaldata[:, :-1], normaldata[:, -1], test_size=0.2, shuffle=False)

print(X_train)

clf = SVR()
clf.fit(X_train, Y_train)
Y_predict = clf.predict(X_test)
print(Y_predict)

def inverse_transform_single(standard, initital, colume):
    initital = initital.copy()
    initital -= standard.min_[colume]
    initital /= standard.scale_[colume]
    return initital


stockdatawithsentiment = pd.read_csv('+-stock_sentiment_data.csv')
col_n = stockdatawithsentiment.shape[1]-2
initialY_predict = inverse_transform_single(standard, Y_predict, col_n)
initialY_Test = inverse_transform_single(standard, Y_test, col_n)
initialY_train = inverse_transform_single(standard, Y_train, col_n)


Y_train_length = initialY_train .shape[0]
Y_length = Y_train_length+initialY_predict.shape[0]
plt.plot(initialY_Test, color='b', label='Sample')
plt.plot(initialY_predict, color='r', label='Predict')

# ax=plt.gca()  #gca:get current axis得到当前轴
# #设置图片的右边框和上边框为不显示
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')

# plt.title('Stock Price Prediction without Sentiment -LSTM')
# plt.legend(loc='lower')
plt.legend(bbox_to_anchor=(0.5, -0.15), loc=8, ncol=2, frameon=False)#  borderaxespad=0
# plt.xlabel('Time Point')
# plt.ylabel('Close')
plt.savefig("picture/SVM有.png", dpi=500, bbox_inches='tight')  #  解决图片不清晰，不完整的问题


# 真实曲线绘制
# plt.plot(np.concatenate([initialY_train, initialY_Test]), color='r', label='sample')
# # 预测曲线绘制
# plt.plot([x for x in range(Y_train_length, Y_length)], initialY_predict, color='g', label='predict')
# plt.title('SVM Prediction of Stock Prices with Sentiment')
# plt.xlabel('date')
# plt.ylabel('close')
# plt.legend()
# plt.tick_params(labelsize=8)
# xticks = np.arange(0, Y_length, 100)
# xtick_labels = [stockdatawithsentiment['date'].values[x][2:] for x in xticks]
# plt.xticks(ticks=xticks, labels=xtick_labels, rotation=25)
Sentiment_Test = [int(c) for c in initialY_Test]
Sentiment_Predict = [int(c) for c in initialY_predict]


normaldata = normaldata.astype(np.float32)
Sentiment_Test = np.array(Sentiment_Test).astype(np.float64)
Sentiment_Predict = np.array(Sentiment_Predict).astype(np.float64)
mse = mean_squared_error(Sentiment_Test, Sentiment_Predict)

print("Sentiment_data\'s mean_absolute_error:", mean_absolute_error(Sentiment_Test, Sentiment_Predict))
print("Sentiment_data\'s mean_squared_error:", mean_squared_error(Sentiment_Test, Sentiment_Predict))
print("Sentiment_data\'s rmse:", sqrt(mean_squared_error(Sentiment_Test, Sentiment_Predict)))
print("Sentiment_data\'s r2 score:", r2_score(Sentiment_Test, Sentiment_Predict))
plt.show()

