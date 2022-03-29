from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.com/news"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

subject = doc.find_all("h3")
for index, link in enumerate(subject):
    print(f"{index + 1}. {link.string}")