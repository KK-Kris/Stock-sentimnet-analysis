import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import numpy as np
import jieba as jb

df = pd.read_csv('project_data/60000comments.csv', encoding='gbk')  # header=0表示第一行是表头，就自动去除了
print(df)
title = df['title']
print(title)
words = []
for i in df['title']:
    comment = list(jb.cut(str(i)))
    words.extend(comment)
print('相同类型股票评论单词数量：', len(words))
print('相同类型股票评论不重复单词数量：', len(set(words)))

with open('project_data/stopwords.txt', 'r', encoding="utf8") as stopwords:
    stopword = stopwords.read().split('\n')
stopword = set(stopword)
# print(stopword)
print("停止词的数量：", len(set(stopword)))

words_without_stopword = []
for word in words:
    if word not in stopword:
        words_without_stopword.append(word)
print("去除停止词的评论单词数量", len(words_without_stopword))
print("去除停止词+去重的评论单词数量", len(set(words_without_stopword)))


count = {}
for word in words_without_stopword:
    if word in count:
        count[word] = count[word] + 1
    if word not in count:
        count[word] = 1


for word, count_number in count.items():
    count[word] = count_number/len(words_without_stopword)

top_words = {}
for word in sorted(count, key=count.get, reverse=True)[:1000]:
    top_words[word] = count[word]

print(top_words)

with open('project_data/top1000comment.csv', 'w') as f:
    for word, count in top_words.items():
        f.write("%s,%s\n" % (word, count))

