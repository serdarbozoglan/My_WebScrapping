## We will scrape ScrapingClub Example 3

import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml') 
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for item in items:
    itemName = item.find('h4', class_='card-title').text.strip('\n')
    itemPrice = item.find('h5').text
    print(f"{count}) Price: {itemPrice}, Item Name: {itemName}")
    count += 1 

# pagination part
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None # we want to exlude 'next' or 'previous' page otherwise we will have duplicate pages 
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
print(urls)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml') 
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for item in items:
        itemName = item.find('h4', class_='card-title').text.strip('\n')
        itemPrice = item.find('h5').text
        print(f"{count}) Price: {itemPrice}, Item Name: {itemName}")
        count += 1 
