import numpy as np
from bs4 import BeautifulSoup
import urllib.request
from nlp_ext_sum import sentence_split, lowercase, cleaning, token, word_freq, sentence_weight

# Example
url = 'https://www.cnn.com/2021/03/05/world/mars-perseverance-rover-first-drive-scn-trnd/index.html'
num = 4

def summarize(url, number_of_sentences):
    r = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(r, 'html.parser')
    news = ''
    article = soup.find_all("div", class_="zn-body__paragraph")
    for paragraph in article:
        news = news + paragraph.text
    sentence_list = sentence_split(news)
    data = []
    for sentence in sentence_list:
        data.append(token(cleaning(lowercase(sentence))))
    data = (list(filter(None, data)))

    ranking = sentence_weight(data)

    # return n-number of sentences in summary
    n = number_of_sentences
    result = ''
    sort_list = np.argsort(ranking)[::-1][:n]
    for i in range(n):
        result += '{} '.format(sentence_list[sort_list[i]])
    return result

summarize(url, num)
