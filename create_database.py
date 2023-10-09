import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import re


keyword_dict = {}
#TODO create database, dict to csv?
#TODO append to list for dict values not only one recipe for key
#for word in title:
#    if not (word in ["and", "the", "or", "of", "by"]):
#        keyword_dict[word] = (title, web_info)

to_print = ""

URL = "https://directionsforme.org/product/0"
r = requests.get(URL)
og_soup = BeautifulSoup(r.content, 'html5lib')
og_title = og_soup.find("title")

index = 264844 #goes up to 264847
more_products = True

while True: #currently about 3.1 pages/sec (264847 total so one whole day uh)
    recipe = ""
    URL = f'https://directionsforme.org/product/{index}'
    r = requests.get(URL)
    current_soup = BeautifulSoup(r.content, 'html5lib')
    current_title = current_soup.find("title")
    if og_title == current_title:
        break
    header = str(current_title).split("<title>")[1].split("</title>")[0]
    recipe += header+ "\n\n"
    for tags in current_soup.find_all("h3"):
        for sib in tags.next_siblings:
            if sib.name=="a":
                break
            sib_clean = sib.text.replace('\n','').replace('\t','').replace(' ', '')
            if tags.text == "Nutrition Facts" and sib_clean != '': #TODO why is it their thrice
                res = str(re.sub('\t', '', sib_clean))
                res = res.strip("\n")
                res = str(re.sub('\n\n\n\n\n\n', '\n', res))
                res = str(re.sub('\n\n\n', ': ', res))
                res = str(re.sub('Title', '', res))
                res = res.strip("\n")
                res = str(re.sub('\n\n', ', ', res))
                recipe += "Nutrition Facts\n" + res.strip("\n") + "\n\n"
            elif tags.text != "Nutrition Facts" and tags.text != "UPC" and sib_clean != '':
                res = re.sub('â€™', '\'', sib_clean)
                recipe += tags.text + "\n" + res.strip("\n").strip("\t").strip("\n") + "\n\n"
    index += 1


with open("database_output.txt", "w") as f:
    f.writelines(f'{to_print}')