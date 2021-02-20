from bs4 import BeautifulSoup
import urllib.request

def scraper(url):
    r = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(r, 'html.parser')
    text = ''
    data = soup.find_all("div",class_="zn-body__paragraph")
    for paragraph in data:
        text = text + paragraph.text
    return text


