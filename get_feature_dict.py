import timeit
import nltk
# from collections import defaultdict
# from sklearn.feature_extraction.text import CountVectorizer
import json
import re, string

start = timeit.default_timer()

data = open('oneyear.json', 'r')

#output file
feature_dict_file = open('feature.txt','w')

visited = set()
messages = []
for line in data:
    tweet = json.loads(line.decode('utf-8'))
    message = tweet['text']
    message = re.sub('https?:\/\/.*[\r\n]*','',message)
# for tweet in messages:
#     messages_file.write(tweet)
#     messages_file.write('\n')

    tokens = nltk.word_tokenize(message)
    for token in tokens:
        if token not in visited:
            visited.add(token)
            feature_dict_file.write(token.encode('ascii','ignore'))
            feature_dict_file.write('\n')

