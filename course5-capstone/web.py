import requests
from bs4 import BeautifulSoup

URL = "https://seenunseen.in/episodes/2022/2/14/episode-264-barun-mitra-philosopher-and-practitioner/"
page = requests.get(URL)
#print(page.content)

soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
#print(list(soup.children))
tags = soup.find_all('a').get_text()
for tag in tags:
    print(tag)

# Retrieve all of the anchor tags
#tags = soup('br')
#print(soup)
#for tag in tags:
    #print(tag.get('href', None))
    #print(tag)
