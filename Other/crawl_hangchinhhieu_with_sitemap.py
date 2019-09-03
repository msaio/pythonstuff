import requests
import json
import os

# import sys
# from importlib import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup

def get_price(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
    results = soup.find_all('p', attrs={'class':'item price'})
    price = results[0].find('span', attrs={'id':'pdPriceNumber'}).text
    return price

f1 = open("hangchinhhieu.json", "w")
f1.write("[")
f1.close()

url = "https://hangchinhhieu.vn/sitemap_products_1.xml"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'xml')
results = soup.find_all('url')
i = 2
while (i < len(results)):
    link = results[i].find('loc').text
    price = get_price(link)
    image = results[i].find('image:loc').text
    title = results[i].find('image:title').text
    print(i)
    print(link)
    print(price.encode('utf-8'))
    print(image)
    print(title.encode('utf-8'))
    record = {"link":link, "price":price, "image":image, "title": title}
    f = open("hangchinhhieu.json", "a")
    if(i == len(results)-1): 
        f.write(json.dumps(record)+"\n")
    else:
        f.write(json.dumps(record)+","+"\n")
    f.close()
    i = i + 1

f1 = open("hangchinhhieu.json", "a")
f1.write("]")
f1.close()
os.system("cp hangchinhhieu.json temp.json")
