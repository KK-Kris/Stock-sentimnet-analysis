# 读取数据
from math import sqrt

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

stockdatawithsentiment = pd.read_csv('+-stock_sentiment_data.csv', index_col='date')
stockdatawithsentiment['volume'] = [int(c.replace(",", "")) for c in stockdatawithsentiment['volume']]

plt.plot(stockdatawithsentiment['close'].values, color='r')
plt.title('Stock Close Data')
plt.xlabel('Time Point')
plt.ylabel('Close')
plt.legend()
# plt.tick_params(labelsize=8)
# xticks = np.arange(0, stockdatawithsentiment.shape[0], 100)
# xtick_labels = stockdatawithsentiment['date'].values[2:]
# plt.xticks(ticks=xticks, labels=xtick_labels, rotation=25)
plt.show()