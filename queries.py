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

def find_product_query(search_input):
    words = search_input.split(" ")
    length = len(words)
    searches = []
    links = []
    titles = []
    for i in range(length):
        for j in range(length):
            word1 = words[i]
            word2 = words[j]
            if not (word1 in ["and", "the", "or", "of", "by", "directions", "for", "me"]):
                if not (word2 in ["and", "the", "or", "of", "by", "directions", "for", "me"]):
                    if i != j:
                        searches.append(f"{words[i].lower()} {words[j].lower()}")
                    else:
                        searches.append(f"{words[i].lower()}")
    for search in searches:
        search_string = ""
        for word in search.split(" "):
            word = word.lower()
            search_string += word + "+"
        search_string = search_string[:-1]
        URL = f"https://directionsforme.org/search/results?search_string={search_string}&_token=YVK8q66vCLRdYiQhbzFi2xqxFvs10TdXLH4JD7Wf"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        soup_links = [node.get('href') for node in soup.find_all("a")]
        for link in soup_links:
            link = str(link)
            if "https://directionsforme.org/product/" in link:
                links.append(link)
        for tag in soup.findAll("h2"):
                titles.append(tag.text)

    link_count = {}
    link_title = {}
    for i in range(len(links)):
        link = links[i]
        if link in link_count.keys():
            link_count[link] = link_count[link] + 1
        else:
            link_count[link] = 1
            link_title[link] = titles[i]


    if links == []:
      resd = OrderedDict()
      website = str(google(search_input))
      resd[f"Google Search for {search_input.upper()}"] = website
      if website == "error":
         return [OrderedDict(), 0]
      return [resd, 1]
    else:
      sorted_list = sorted(link_count.items(), key=lambda x:x[1], reverse=True)       
      count = min(10,len(links))
      resd = OrderedDict()
      for i in range(count):
        link = sorted_list[i][0]
        title = link_title[link]
        resd[title] = webscrape(link)
    return [resd, count]

#print(find_product_query("kraft mac and cheese"))