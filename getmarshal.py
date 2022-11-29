from snownlp import sentiment
sentiment.train('project_data/negative_snownlp+mine.txt', 'project_data/posositive_snownlp+mine.txt')
# sentiment.train('neg_title.txt', 'pos_title.txt')
sentiment.save('sentiment.marshal')

