import requests
from bs4 import BeautifulSoup
import csv
<<<<<<< HEAD
=======
from collections import OrderedDict
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41


def find_product(search_input):
<<<<<<< HEAD
    #convert database in csv to dict TODO move to webapp.py for efficiency
    d = {}
    with open('database263000.csv', 'r') as db:
=======
    db_name = "database263000.csv"
    #convert database in csv to dict TODO move to webapp.py for efficiency
    d = {}
    with open(db_name, 'r') as db:
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
       rdr = csv.reader(db)
       next(rdr)
       for row in rdr:
          d[row[0]] = row[1:]

    to_print = ""

    recipe_count = {}
    words = search_input.split(" ")
    for word in words:
        if not (word.lower() in ["and", "the", "or", "of", "by", "directions", "for", "me"]):
           if word in d.keys():
              recipes = d[word]

              for recipe in recipes:
                to_print += recipe
                if recipe in recipe_count.keys():
                    recipe_count[recipe] = recipe_count[recipe] + 1
                else:
                    recipe_count[recipe] = 1
<<<<<<< HEAD
                 
    sorted_list = sorted(recipe_count, reverse=True)
    #with open("temp_output.txt", "w") as f: #temp writing output to file TODO delete    
        #f.writelines(to_print)
    #    f.writelines(f'{len(sorted_list)}')

    return [{"test": "test.html"}, len(sorted_list)]

find_product("True")
=======

    #if recipe_count == {}: TODO
    #   return google(search_input)
                 
    sorted_list = sorted(recipe_count, reverse=True)
    count = min(10,len(sorted_list))

    resd = OrderedDict()
    for elem in sorted_list:
       title = bytes(elem, 'utf-8').split(b'\n')[0].decode("utf-8")
       resd[title] = elem

    return [resd, count]

>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41

#webscrapes and outputs website info given input link
def print_link(search_input):
   url = search_input.strip()
   resp=requests.get(url)
   #http_response 200 means OK status
   if resp.status_code==200: #if link
      return resp.content #TODO take only important parts
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