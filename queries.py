import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from websearch import google
import re
from datetime import datetime


def webscrape(URL):
    directions = ""
    r = requests.get(URL)
    current_soup = BeautifulSoup(r.content, 'html5lib')
    for tags in current_soup.find_all("h3"):
        for sib in tags.next_siblings:
            if sib.name=="a":
                break
            sib_clean = sib.text.replace('\n','').replace('\t','*').replace(' ', '')
            cond = sib_clean.replace("*", "")
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
    return directions

#true grit error TODO

def find_product_query(search_input):
    search_string = ""
    for word in search_input.split(" "):
        word = word.lower()
        search_string += word + "+"
    search_string = search_string[:-1]
    URL = f"https://directionsforme.org/search/results?search_string={search_string}&_token=YVK8q66vCLRdYiQhbzFi2xqxFvs10TdXLH4JD7Wf"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    soup_links = [node.get('href') for node in soup.find_all("a")]
    links = []
    for link in soup_links:
        link = str(link)
        if "https://directionsforme.org/product/" in link:
            links.append(link)
    titles = []
    for tag in soup.findAll("h2"):
            titles.append(tag.text)

    if links == []:
      resd = OrderedDict()
      website = str(google(search_input))
      resd[f"Google Search for {search_input.upper()}"] = website
      if website == "error":
         return [OrderedDict(), 0]
      return [resd, 1]
    else:          
      count = min(10,len(links))
      resd = OrderedDict()
      for i in range(count):
        title = titles[i]
        resd[title] = webscrape(links[i])
    return [resd, count]
