from bs4 import BeautifulSoup
import requests

#getting the link  of ebay (new nearby manga sell offers)
source = requests.get('https://www.ebay-kleinanzeigen.de/s-gescher/manga/k0l1332r20').text
soup = BeautifulSoup(source, 'lxml')

#scraping title
title = soup.title.text

from collections import namedtuple
Item = namedtuple("Item", "title price city date")

items = []

#scraping all information regarding offers
for item in soup.select(".aditem"):
    title = item.select_one(".ellipsis").text
    information = item.select_one(".aditem-details").text
    information = information.strip()
    information = information.split()
    #"VB" is as first index and normal price (1,€) as first two indexes
    price = information[0] + information[1] if information[0] != "VB" else information[0]
    #depending on "VB" the index of city changes (if city has 2 words or more in it then it only takes the first one)
    if information[0] == 'VB':
        city = information[2]
    elif information[2] == 'VB':
        city = information[4]
    else:
        city = information[3]
    date = item.select_one(".aditem-addon").text.strip()

    items.append(Item(title, price, city, date))

str_items = ""
for item in items:
    str_items += item.title + " | " + item.price + " | " + item.city + " | " + item.date + '\n'

from datetime import date
today = date.today()
today = today.strftime("%d %B")

#creating a file with results
with open("Manga on Ebay - "+today+".txt", 'w') as fw:
    fw.write(title+'\n\n')
    fw.write(str_items)




