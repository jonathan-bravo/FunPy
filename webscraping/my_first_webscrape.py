#!/usr/bin/env python3

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

# Opening up the page, loading it into a variable, and then closing the connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})
# finding item branding within item newegg
item_brand = page_soup.findAll("a",{"class":"item-brand"})
# finding item titles within newegg
item_titles = page_soup.findAll("a",{"class":"item-title"})
# find item shipping within newegg
price_ship = page_soup.findAll("li",{"class":"price-ship"})

filename = "graphics_cards.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

# Finds the brands of the graphics cards
for i in range(0,len(containers)):
	f.write(item_brand[i].img["title"] + "," + item_titles[i].text.strip().replace(",", "|") + "," + price_ship[i].text.strip() + "\n")

f.close()