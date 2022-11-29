import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import numpy as np
import jieba as jb

df = pd.read_csv('project_data/60000comments.csv', encoding='gbk')  # header=0表示第一行是表头，就自动去除了
print(df)
title = df['title']
print(title)

keyweight = pd.read_csv('project_data/keyweight1000.csv', encoding='gbk')
keyweight.columns = ['word', 'posORneg']
print(keyweight)
print(keyweight.shape)

positive_word = keyweight.loc[keyweight['posORneg'] == 1, 'word'].to_list()
print(positive_word)
pos_word = [c.replace("\n", "") for c in positive_word]
print(pos_word)
negative_word = keyweight.loc[keyweight['posORneg'] == -1, 'word'].to_list()
neg_word = [c.replace("\n", "") for c in negative_word]
print(neg_word)

neutral_word = keyweight.loc[keyweight['posORneg'] == 0, 'word'].to_list()
neu_word = [c.replace("\n", "") for c in neutral_word]
print(neu_word)

count = {}
for title in df['title']:
    title_words = jb.cut(str(title))
    for word in title_words:
        if word in pos_word:
            if title in count:
                count[title] = count[title] + 1
            if title not in count:
                count[title] = 1
        if word in neg_word:
            if title in count:
                count[title] = count[title] - 1
            if title not in count:
                count[title] = -1
        if word in neu_word:
            if title in count:
                count[title] = count[title]
            if title not in count:
                count[title] = 0
    if title not in count:
        count[title] = 0
    print("one title is OK")


print(count)

pos_title = []
neg_title = []
neu_title = []
for title in df['title']:
    print(title)
    if count[title] > 0:
        pos_title.append(title)
    if count[title] == 0:
        neu_title.append(title)
    if count[title] < 0:
        neg_title.append(title)

print(pos_title)
print(neg_title)
# print(neu_title)
print(len(pos_title))
# print(len(neu_title))
print(len(neg_title))

with open('project_data/pos_title.txt', 'w', encoding='utf-8') as f:
    for title in pos_title:
        f.write(title+"\n")
f.close()

with open('project_data/neg_title.txt', 'w', encoding='utf-8') as f:
    for title in neg_title:
        f.write(title+"\n")
f.close()