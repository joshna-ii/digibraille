import requests
from bs4 import BeautifulSoup
from datetime import datetime

#TODO figure out how to make this fast

to_print = ""

URL = "https://directionsforme.org/product/0"
r = requests.get(URL)
og_soup = BeautifulSoup(r.content, 'html5lib')
og_title = og_soup.find("title")

index = 1
more_products = True

while more_products: #currently about 3.1 pages/sec (264847 total so one whole day uh)
    URL = f'https://directionsforme.org/product/{index}'
    r = requests.get(URL)
    current_soup = BeautifulSoup(r.content, 'html5lib')
    current_title = current_soup.find("title")
    if og_title == current_title:
        more_products = False
    if(index == 500):
        more_products = False
    index += 1
    print(index)


with open("temp_output.txt", "w") as f:
    f.writelines(f'{to_print}')