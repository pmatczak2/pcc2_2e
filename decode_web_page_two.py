from bs4 import BeautifulSoup
import requests


url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

for index in soup.find_all('p'):
    print(index.text)

