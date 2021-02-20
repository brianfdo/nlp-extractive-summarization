import numpy as np
import nltk
import re

# casefold sentence
def lowercase(sentence):
    return sentence.lower()

# remove unwanted chars
def cleaning(sentence):
    return re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))

# tokenize sentence
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

# rank
def sentence_weight(data):
    weights = []
    wordfreq = word_freq(data)
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        weights.append(temp)
    return weights
