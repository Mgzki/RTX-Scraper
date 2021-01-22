import os
from datetime import datetime
from re import compile
from re import match


import requests
from bs4 import BeautifulSoup

def stock_numbers(URL):
    #page = requests.get('https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183101')
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    stock_values = soup.find_all('div', class_='col-3 justify-content-end')
    locations = soup.find_all('div', class_='col-9')

    stock = []
    for i in range(len(stock_values)):
        stock.append(stock_values[i].get_text())
        stock[i] = stock[i].strip('\n')

    store = []
    for i in range(len(locations)):
        store.append(locations[i].get_text())
        store[i] = store[i].strip('\n')
    val = ''
    while val in stock or val in store:
        stock.remove(val)
        store.remove(val)

    return list(zip(store,stock))

def all_locations():

    URLS = [
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183101',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183560',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183500',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183100',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183636',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183561',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=184168',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183638',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=184743',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183208',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183499',
    'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183099'
    ]
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if os.path.exists("rtx3070-Stock.txt"):
        os.remove("rtx3070-Stock.txt")
    f = open("rtx3070-Stock.txt", "w")
    
    for url in URLS:
        f.write("\n" + current_time + "\n" + url)
        temp = stock_numbers(url)
        stock_info = []
        for i in range(len(temp)):
            stock_info.append(temp[i])
        for i in range(len(stock_info)):
            f.write("\n" + stock_info[i][0] + " : " + stock_info[i][1] + ' (' + url + ')')

if __name__ == '__main__':
    all_locations()