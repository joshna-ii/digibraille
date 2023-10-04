from googlesearch import search
import requests
from bs4 import BeautifulSoup

def find_product(search_input):
    #looks through directions for me and similar websites for keywords
    #uses the google function
    #jk need to create database and will only use google function if not in database
    return "working on in temp code file"


def print_link(search_input):
   url = search_input.strip()
   resp=requests.get(url)
      
   #http_respone 200 means OK status
   if resp.status_code==200: #if link
      return resp.content #TODO take only important parts
   else:
      return "error"


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

