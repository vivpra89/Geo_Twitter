import timeit
import nltk
# from collections import defaultdict
# from sklearn.feature_extraction.text import CountVectorizer
import json

start = timeit.default_timer()

data = open('oneyear.json', 'r')

#output file
feature_dict_file = open('feature.txt','w')

visited = set()
for line in data:
    tweet = json.load(line.decode('utf-8'))

    tokens = nltk.word_tokenize(tweet['test'])
    for token in tokens:
        if token not in visited:
            visited.add(token)
            feature_dict_file.write(token)
            feature_dict_file.write('\n')

