import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import re
import csv


keyword_dict = {}
URL = "https://directionsforme.org/product/0"
r = requests.get(URL)
og_soup = BeautifulSoup(r.content, 'html5lib')
og_title = og_soup.find("title")

start_index = 118746 #goes up to 264847
more_products = True
index = start_index

while True: #currently about 3.1 pages/sec (264847 total so one whole day uh)
    directions = ""
    URL = f'https://directionsforme.org/product/{index}'
    r = requests.get(URL)
    current_soup = BeautifulSoup(r.content, 'html5lib')
    current_title = current_soup.find("title")
    if og_title == current_title:
        break
    title = str(current_title).split("<title>")[1].split("</title>")[0]
    directions += title + "\n\n\n"
    for tags in current_soup.find_all("h3"):
        for sib in tags.next_siblings:
            if sib.name=="a":
                break
            sib_clean = sib.text.replace('\n','').replace('\t','*').replace(' ', '')
            cond = sib_clean.replace("*", "").strip()
            if tags.text == "Nutrition Facts" and cond != '':
                sib_clean = re.sub(r'[*]{1,44}', ':', sib_clean).replace("::","\n")
                res = str(re.sub('\t', '', sib_clean))
                res = res.strip("\n")
                res = str(re.sub('\n\n\n\n\n\n', '\n', res))
                res = str(re.sub('\n\n\n', ': ', res))
                res = str(re.sub('Title', '', res))
                res = res.strip("\n")
                res = str(re.sub('\n\n', ', ', res))
                directions += "Nutrition Facts\n" + res.strip("\n") + "\n\n"
            elif tags.text != "Nutrition Facts" and tags.text != "UPC" and cond != '':
                res = re.sub('â€™', '\'', cond)
                directions += tags.text + "\n" + res.strip("\n").strip("\t").strip("\n") + "\n\n"
            
    index += 1
    print(index)

    for word in title.split(" "):
        if not (word.lower() in ["and", "the", "or", "of", "by", "directions", "for", "me"]):
            if word not in keyword_dict.keys():
                keyword_dict[word] = directions
            else:
                keyword_dict[word] = keyword_dict[word] + "new_elem_for_list" + directions


with open(f'database{start_index}.csv', 'w', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(["keyword", "recipe1", "recipe2", "recipe3"])
    for key in keyword_dict:
        l = [key]
        for e in keyword_dict[key].split("new_elem_for_list"):
            l.append(e)
        writer.writerow(l)
