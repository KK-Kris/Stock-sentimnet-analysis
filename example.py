import pandas as pd

comments = pd.read_csv("688180comments.csv", encoding='GBK')
print(comments[-50:-22])
stockdatawithsentiment = pd.read_csv('+-stock_sentiment_data.csv', index_col='date')
print(stockdatawithsentiment[4:10])