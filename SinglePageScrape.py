## we will scrape quotes.toscrape.com

import requests
import lxml
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text') # do not forget _ after classs
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags') # this grabs all tags for a quote
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag') # we grab every tag under a quote
    for quoteTag in quoteTags:
        print(quoteTag.text)
