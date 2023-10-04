import requests
from bs4 import BeautifulSoup


keyword_dict = {}
#for word in title:
#    if not (word in ["and", "the", "or", "of", "by"]):
#        keyword_dict[word] = details

to_print = ""

URL = "https://directionsforme.org/product/0"
r = requests.get(URL)
og_soup = BeautifulSoup(r.content, 'html5lib')
og_title = og_soup.find("title")

index = 264847
more_products = True

while True: #currently about 3.1 pages/sec (264847 total so one whole day uh)
    URL = f'https://directionsforme.org/product/{index}'
    r = requests.get(URL)
    current_soup = BeautifulSoup(r.content, 'html5lib')
    current_title = current_soup.find("title")
    if og_title == current_title:
        break
    header = str(current_title).split("<title>")[1].split("</title>")[0]
    for tags in current_soup.find_all("h3"):
        for sib in tags.next_siblings:
            if sib.name=="a":
                break
            to_print += str(tags.text) + str(sib)
    #to_print += str(current_soup)
    index += 1


with open("database_output.txt", "w") as f:
    f.writelines(f'{to_print}')