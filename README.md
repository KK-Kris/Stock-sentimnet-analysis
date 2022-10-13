# Stock-sentimnet-analysis

# provide a new method for the Chinese stock comment sentiment analysis

SnowNLP is a corpus-based model that automatically counts word sentiment polarity to judge text sentiment by using corpus of related fields and correlation calculation rules combined with machine learning. The official point out that the high accuracy of e-commerce comments is because its corpus is mainly e-commerce comments data. So at this coding, we have change the e-commerce comments into the Chinese Stock's comments.
  This repository  have using the combination of the emotional dictionary and the machine learning to analysis the target stock's sentiment.
  Depends on the two-hour leading ability of investor sentiment to predict price.vWe get the stock hour line data, EastMoney Gub's comment which predictiong needs, and the stopwords that need to divide words from sentence.
  Stock in the same industry to help us get the most frequent 1000 words which needs we manually label the characteristic. That words is a part of emotional dictionary.
After the combine the frequent words and the emotional dictionary as a new dictionary, we use the new dictionary to label the comment's characteristic.
  When we get the new positive and negetive corpus, we retrain the SnowNLP .marshal to help us classify the stock comment and get the sentiment index which give us a very important index to predict the stock price.
  For processing the stock sentiment, we get the average of sentiment of comment two hours before the time point.
  We get this repository to provide a new method to give a predict about the JunShi Biological and we will test the accuracy between the real value and the predict value to find the value of sentiment index.
  
  
