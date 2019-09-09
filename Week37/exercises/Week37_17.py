import re
from requests import get
from bs4 import BeautifulSoup

FEED = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

res = get(FEED)
soup = BeautifulSoup(res.text, 'xml')
headlines = soup.find_all('title')
for h in headlines:
    print(h.contents[0])