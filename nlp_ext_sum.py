import numpy as np
import nltk
import re
import scraper

def lowercase(sentence):
    return sentence.lower()

def cleaning(sentence):
    return re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))

def token(sentence):
    return sentence.split()

def sentence_split(paragraph):
    return nltk.sent_tokenize(paragraph)

def word_freq(data):
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    wordbag = list(set(w))
    assign = {}
    for word in wordbag:
        assign[word] = w.count(word)
    return assign

def sentence_weight(data):
    weights = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        weights.append(temp)
    return weights

news = scraper(url)
sentence_list = sentence_split(news)
data = []
for sentence in sentence_list:
    data.append(token(cleaning(lowercase(sentence))))
data = (list(filter(None, data)))

wordfreq = word_freq(data)

ranking = sentence_weight(data)

# return n-number of sentences in summary
n = 2
result = ''
sort_list = np.argsort(ranking)[::-1][:n]
for i in range(n):
    result += '{} '.format(sentence_list[sort_list[i]])

print(result)