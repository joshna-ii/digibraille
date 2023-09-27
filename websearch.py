from googlesearch import search
import requests
from bs4 import BeautifulSoup



x = search("help")
print(x)


search = 'presidents'
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

#print(first_link['href'])




url='https://www.myfoodandfamily.com/recipe/056248/kraft-macaroni-cheese-dinner'
      
#open with GET method
resp=requests.get(url)
      
#http_respone 200 means OK status
if resp.status_code==200:
    #print("Successfully opened the web page")
    print("The news are as follow :-\n")
    print(resp.text[:400])
      
    # we need a parser,Python built-in HTML parser is enough .
    #soup=BeautifulSoup(resp.text,'html.parser')    
  
    # l is the list which contains all the text i.e news 
    #l=soup.find("ul",{"class":"searchNews"})
      
    #now we want to print only the text part of the anchor.
    #find all the elements of a, i.e anchor
    #for i in l.findAll("a"):
    #    print(i.text)
else:
    print(resp)