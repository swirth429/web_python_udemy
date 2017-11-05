__author__ = 'swirth'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/herman-miller-classic-aeron-office-chair/p230630306")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price"})

string_price = element.text.strip()
price_without_symbol = string_price[1:]

print(float(price_without_symbol))

#print(element.text.strip())
#<p class="price"><strong class="simpleNowPrice">899.00</strong></p>
#print(content)