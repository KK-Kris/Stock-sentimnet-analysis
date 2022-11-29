import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import int16
# from snownlp import SnowNLP
import numpy as np

# from keras.losses import mean_absolute_error, mean_squared_error
# from sklearn.metrics import r2_score

sentiment = pd.read_csv('feature_data.csv')
sentiment.columns = ['date', 'open', 'high', 'low', 'volume', 'sentiment']
print(sentiment)

# data = sentiment['open', 'high', 'low', 'close', 'volume', 'sentiment']
# print(data)
sentiment_corr = sentiment.corr()
print(sentiment_corr)
plt.figure(1)
sns.heatmap(sentiment_corr, annot=True, vmax=1, square=True)  # 绘制df_corr的矩阵热力图
plt.show()  # 显示图片
## 相关性低是好事
