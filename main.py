import json
import requests
from bs4 import BeautifulSoup

x = requests.get("https://www.sas.am/en/")
y = BeautifulSoup(x.text, "html.parser")

anchors = y.select(".main-menu__link-level-3")
products = {}
for a in anchors:
    name = a.text
    url = "https://www.sas.am" + a['href'] + "?SORTBY=PRICE_LOW"
    products[name] = url


def minprice(name):
    z = requests.get(products[name])
    ztext = BeautifulSoup(z.text, 'html.parser')
    items = ztext.select(".catalog__col")
    for i in items:
        product_name = i.select_one(".product__name").text
        price = i.select_one(".price__text").text
        print(product_name + "   " + price)


minprice("Coffee")
