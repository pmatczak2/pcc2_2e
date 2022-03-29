from bs4 import BeautifulSoup
import requests, re

result = requests.get('https://www.nytimes.com/')

src = result.content
soup = BeautifulSoup(src, 'lxml')

headings = soup.find_all(re.compile("^h[1-2]$"), {'class': "story-wrapper"})
for link in headings:
    print(link)
