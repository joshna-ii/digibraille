import requests
from bs4 import BeautifulSoup
import csv
from collections import OrderedDict


def find_product_database(search_input, db):

    to_print = ""

    recipe_count = {}
    words = search_input.split(" ")
    for word in words:
        if not (word.lower() in ["and", "the", "or", "of", "by", "directions", "for", "me"]):
           if word in db.keys():
              recipes = db[word]

              for recipe in recipes:
                to_print += recipe
                if recipe in recipe_count.keys():
                    recipe_count[recipe] = recipe_count[recipe] + 1
                else:
                    recipe_count[recipe] = 1
    
    with open("recipes.txt", "w") as f:
        f.writelines(f'{recipe_count}')

    if recipe_count == {}:
      resd = OrderedDict()
      website = str(google(search_input))
      resd[f"Google Search for {search_input.upper()}"] = website
      if website == "error":
         return [OrderedDict(), 0]
      return [resd, 1]
    else:          
      sorted_list = sorted(recipe_count, reverse=True)
      count = min(10,len(sorted_list))
      resd = OrderedDict()
      for elem in sorted_list:
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
    return print_link(first_link['href'])
