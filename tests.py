from translation import contracted_translation, pretty_print_trans
import string
import random
from datetime import datetime
import csv
import requests
from bs4 import BeautifulSoup
import re
from websearch import find_product_database, find_product_query


def uncontracted_translation_test(): #TODO test with real words too
    #TODO make this a loop
    # initializing size of string
    N = 7
    # generating random strings
    res = ''.join(random.choices((string.ascii_letters + string.digits), k=N))#TODO string.punctuation

    trans = contracted_translation(res)

    with open("tests_output.txt", "w") as f:
        f.write(f'TEST STRINGS\n')
    with open("tests_output.txt", "a") as f:
        f.write(f'{res}\n')
    with open("tests_output.txt", "a") as f:
        f.write(f'\n\nOUTPUTS\n')
    with open("tests_output.txt", "a") as f:
        f.write(f'{pretty_print_trans(trans)}\n\n')

uncontracted_translation_test()

#TODO only double cap if more than one in a row

db_creation_time_sum = 0
db_creation_time_count = 0

for i in range(5):
    dbcreationtime1 = datetime.now()
    #create database
    db_name = "database1.csv" #specify csv file with database
    db = {}
    with open(db_name, 'r') as db_file:
        rdr = csv.reader(db_file)
        next(rdr)
        for row in rdr:
            db[row[0]] = row[1:]
    dbcreationtime2 = datetime.now()
    db_creation_time_sum += float(str(dbcreationtime2-dbcreationtime1).split(":")[2])
    db_creation_time_count += 1
with open("tests_output.txt", "a") as f:
    f.write(f'AVERAGE DATABASE SETUP TIME: {db_creation_time_sum/db_creation_time_count} seconds\n\n')

[result, count] = find_product_database("chobani", db)

#get 100 most popular products
URL = f'https://progressivegrocer.com/100-iconic-brands-changed-grocery'
r = requests.get(URL)
wiki_soup = BeautifulSoup(r.content, 'html5lib')
x = wiki_soup.findAll("h2")
final_list = []
for elem in x:
    y = str(elem).split(". ")
    if len(y) > 1:
        inp = y[1].split("</h2>")[0].split(" (")[0].split(" (")[0].split("<br/>")[0]
        res = re.sub(r"&amp;", "&", inp)
        final_list.append(res.strip())

database_google_count = 0
db_times_sum = float(0)
db_times_count = 0
with open("tests_output.txt", "a") as f:
    f.write(f'DATABASE PRODUCT SEARCHES\n')
for product in final_list:
    dbsearchtime1 = datetime.now()
    [result, count] = find_product_database(product, db)
    dbsearchtime2 = datetime.now()
    db_times_sum += float(str(dbsearchtime2-dbsearchtime1).split(":")[2])
    db_times_count += 1
    if count == 1:
        database_google_count += 1
    with open("tests_output.txt", "a") as f:
        f.write(f'product searched: {product}\nbeginning of result: {str(result)[:80]}...\n\n')
with open("tests_output.txt", "a") as f:
    f.write(f'\n# of GOOGLE SEARCHES WITH DB: {database_google_count}\n\n')
    f.write(f'AVERAGE DATABASE SEARCH TIME: {db_times_sum/db_times_count} seconds\n\n')


query_google_count = 0
query_times_sum = float(0)
query_times_count = 0
with open("tests_output.txt", "a") as f:
    f.write(f'QUERY PRODUCT SEARCHES\n')
for product in final_list:
    querytime1 = datetime.now()
    [result, count] = find_product_query(product)
    querytime2 = datetime.now()
    query_times_sum += float(str(querytime2-querytime1).split(":")[2])
    query_times_count += 1
    if count == 1:
        query_google_count += 1
    with open("tests_output.txt", "a") as f:
        f.write(f'product searched: {product}\nbeginning of result: {str(result)[:80]}...\n\n')
with open("tests_output.txt", "a") as f:
    f.write(f'\n# of GOOGLE SEARCHES WITH QUERIES: {query_google_count}\n\n')
    f.write(f'AVERAGE QUERY TIME: {query_times_sum/query_times_count} seconds')