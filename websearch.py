import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import re

def webscrape(URL):
    directions = ""
    r = requests.get(URL)
    current_soup = BeautifulSoup(r.content, 'html5lib')
    title = str(current_soup.find("title")).split("<title>")[1].split("</title>")[0]
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
    return [title, directions]

def find_product_query(search_input):
    words = search_input.split(" ")
    length = len(words)
    searches = []
    links = []
    first_search_links = []
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
        for word in search.split(" "): #search_input was search
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
                first_search_links.append(link)
                if search == search_input:
                    links.append(link)
 
    link_count = {}
    for i in range(len(first_search_links)):
        link = first_search_links[i]
        weight = 1
        if link in links:
            weight = 2
        if link in link_count.keys():
            link_count[link] = link_count[link] + (1 * weight)
        else:
            link_count[link] = 1 * weight


    if first_search_links == []:
      resd = OrderedDict()
      website = str(google(search_input))
      resd[f"Google Search for {search_input.upper()}"] = website
      if website == "error":
         return [OrderedDict(), 0]
      return [resd, 1]
    else:
      sorted_list = sorted(link_count.items(), key=lambda x:x[1], reverse=True)   
      count = min(10,len(first_search_links))
      resd = OrderedDict()
      for i in range(count):
        link = sorted_list[i][0]
        [title, directions] = webscrape(link)
        resd[title] = directions
    return [resd, count]


def find_product_database(search_input, db):
    recipe_count = {}
    words = search_input.split(" ")
    for word in words:
        word = word.lower()
        if not (word in ["and", "the", "or", "of", "by", "directions", "for", "me"]):
           if word in db.keys():
              recipes = db[word]
              for recipe in recipes:
                if recipe in recipe_count.keys():
                    recipe_count[recipe] = recipe_count[recipe] + 1
                else:
                    recipe_count[recipe] = 1


    if recipe_count == {}:
      return find_product_query(search_input)
    else:        
      sorted_list = sorted(recipe_count.items(), key=lambda x:x[1], reverse=True)
      count = min(10,len(sorted_list))
      resd = OrderedDict()
      for i in range(count):
         elem = sorted_list[i][0]
         title = bytes(elem, 'utf-8').split(b'\n')[0].decode("utf-8")
         resd[title] = elem

    return [resd, count]


#webscrapes and outputs website info given input link
def print_link(search_input):
   url = search_input.strip()
   resp=requests.get(url)
   #http_response 200 means OK status
   if resp.status_code==200: #if link
      return resp.content
   else:
      return "error"


#searches google for relevant website given keywords
def google(keywords):
    search = keywords
    url = 'https://www.google.com/search'
    headers = {
        'Accept' : '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': search}
    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')
    search = soup.find(id = 'search')
    first_link = search.find('a')
    return (first_link['href'])
