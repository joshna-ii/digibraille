# importing Flask and other modules

from flask import Flask, request, render_template, jsonify, session, request,redirect, url_for
import copy
from flask import Flask, request, render_template
import copy
from main_backend import run_backend
import re
import random 
import csv
from cache import add_cache, create_cache

# Flask constructor
app = Flask(__name__)  
app.secret_key = 'your_secret_key'

#for rpi
database_or_query = "db" #say either "query" or "db"
db_name = "../database1.csv" #specify csv file with database

cache = create_cache()

#create database
db = {}
'''for rpi
if database_or_query == "db":
   with open(db_name, 'r') as db_file:
      rdr = csv.reader(db_file)
      next(rdr)
      for row in rdr:
         db[row[0]] = row[1:]'''
 

# global results 
results  = {}
men_pressed = ""
options_to_display = {}
n = 0
search_input = ""
buttonPressed = False
product_info = {}
button_value = ""
flag = True
button_name = ""
order = ["Result 0", "Result 1", "Result 2", "Result 3", "Result 5"]


sample = """ Product Title

Directions
Product directions. These are the directions

Description
This description is so awesome 

Other Description
Yay more information 

Nutritional Facts
serving size: 2 cups
protein: 30 g
potassium: 200mg

Ingredients
Beef, Water, Seasonings (Spices, Encapsulated Vinegar, Garlic, Paprika, Malt Extract) """

# ensure different sessions for different users using web app at the same time
def generate_unique_identifier():
    # Generate a unique identifier for the user
    return str(random.randint(1, 1000000))

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
   global n, search_input, options_to_display, results
   if 'menu' in request.form:
      # Clear the variable or perform any other action
     # n = 0 
      #search_input = ""
      #options_to_display = {}
      #results = []
      test = 1

   return render_template("website.html")

@app.route('/upload')   
def upload():   
    return render_template("upload.html")   
  
@app.route('/uploaded', methods = ['POST']) 
def uploaded_image():
    global results, options_to_display, product_info, button_value
    if request.method == 'POST':   
        f = request.files['file'] 
        if f.filename != "" and (f.filename[-3:] == "png" or f.filename[-3:] == "jpg" or f.filename[-4:] == "jpeg"):
            f.save(f"images/{f.filename}")
            [results,barcode_detection] = run_backend("upload", f"images/{f.filename}", "", "", "")
            n = 1
            items_per_page = 5
            start_index = 0*items_per_page + 0 
            end_index = 0*items_per_page + 5
            options_to_display = {}
            c = 0 

            for key in results:
               if ( c >= start_index and c < end_index):
                  options_to_display[key] = results[key]
               c += 1 

            return render_template("uploaded.html",barcode_detection=barcode_detection,results=options_to_display)
        else:
            return redirect("/upload", code=302)


# function for typing notes feature on web app
@app.route('/typenotes', methods =["GET", "POST"])
def typenotes():
   if request.path == '/typenotes':
      if request.method == "POST":
         # getting input with notes in HTML form
         notes_input = request.form.get("notes")
         run_backend("notes", notes_input,"","","")
   return render_template("typenotes.html")


@app.route('/clear', methods=['POST'])
def clear_variables():
    global results,n, search_input 

    # Check if the clear button is pressed
    if 'menu' in request.form:
        # Clear the variable or perform any other action
        print("cleared")

    # Redirect back to the index page
    return redirect(url_for('searchproduct'))


# function for searching product feature on webapp
@app.route('/searchproduct', methods =["GET", "POST"])
def searchproduct(page=0):
   global results,n, search_input,flag,cache


   user_id = session.get('user_id')

    # If the user doesn't have a unique identifier, generate one and store it in the session

   
   if request.path == '/searchproduct':
      if (request.method == "POST"):
   
         # getting input with search in HTML form
         search_input = request.form.get("search")

         [results,n] = run_backend("search", search_input,db,database_or_query,cache)
         cache = add_cache(search_input,cache,[results,n])

         items_per_page = 5
         start_index = page*items_per_page + 0 
         end_index = page*items_per_page + 5
         options_to_display = {}
         c = 0 

         for key in results:
            if ( c >= start_index and c < end_index):
               options_to_display[key] = results[key]
            c += 1 

         search_performed = bool(results)
         return render_template("searchproduct.html",order=order,results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)

   if (results == []):
      return render_template("searchproduct.html",current_page=page)
   else:
      items_per_page = 5
      start_index = page*items_per_page + 0 
      end_index = page*items_per_page + 5
      options_to_display = {}
      c = 0 
      search_performed = bool(results)

      for key in results:
         if ( c >= start_index and c < end_index):
            options_to_display[key] = results[key]
         c += 1 
      return render_template("searchproduct.html",order=order, results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)



# function for searching product feature on webapp
@app.route('/nextpage', methods =["GET", "POST"])
def nextpage(results=results):
   global search_input, options_to_display, cache
   page = 1
   if request.path == '/nextpage':
         # getting input with search in HTML form
         if request.method == "POST":
            search_input = request.form.get("search")
         [results,n] = run_backend("search", search_input,db,database_or_query,cache)
         cache = add_cache(search_input,cache,[results,n])

         items_per_page = 5
         start_index = page*items_per_page + 0 
         end_index = page*items_per_page + 5
         options_to_display = {}
         c = 0 

         for key in results:
            if ( c >= start_index and c < end_index):
               options_to_display[key] = results[key]
            c += 1 

         search_performed = bool(results)
         return render_template("nextpage.html",order=order, results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)

   return render_template("nextpage.html",current_page=page,search_input=search_input)

def parse_nutrition(lines,values):
   i = 0
   hit = 0
   nutrition = ""
   nut_dict = {}


   for line in lines:
      values.add(line)
     
      if (line == "Nutrition Facts"):
         hit = 1 
      if (hit == 1 and line):
         if (line != "Nutrition Facts"):
            nutrition += line + """
"""
      if (hit == 1 and line == ''):
         break
   
   rem = ['']; 
   units = ['g', 'mg'] #keep adding if there are more units
   nutr_lines_v1 = re.split(r'[\n,:]', nutrition)
   nutr_lines_v2 = [item for item in nutr_lines_v1 if item not in rem]

   new = ""; 
   nutr_lines = []
   i = 0
   while i < (len(nutr_lines_v2)-1):
      if nutr_lines_v2[i].isnumeric() and nutr_lines_v2[i+1] in units:
         new =  nutr_lines_v2[i] +  nutr_lines_v2[i+1]
         nutr_lines.append(new) 
         i += 2
      else:
         nutr_lines.append(nutr_lines_v2[i]) 
         i += 1 
      

   i = 0 

   while i < len(nutr_lines)-1:
      curr = nutr_lines[i].replace(" ", "")
      val = nutr_lines[i+1][0]
 
      
    
      if curr.isalpha() and val.isnumeric():
         k = i+1
         add = ""
      
         while (val.isnumeric() and k < len(nutr_lines)-1):
            add += (nutr_lines[k]) + " "
            k += 1
            val = nutr_lines[k][0]

         nut_dict[ nutr_lines[i]] = add
         i += 1
      i += 1


   start_index = next((i for i, item in enumerate(lines) if "Nutrition Facts" in item), None)

    # Find the index where "Ingredients" starts
   end_index = next((i for i, item in enumerate(lines) if "Ingredients" in item), None)

    # Extract the portion between "Nutrition Facts" and "Ingredients"
   if start_index is not None and end_index is not None:
      nutrition_facts_data = lines[start_index:end_index]
      # Concatenate the list into a single string
      nutrition_facts_string = '\n'.join(map(str, nutrition_facts_data))
   
   pattern = re.compile(r'(\w+(?:\s\w+)*):\s?([\d.]+(?:\s?[a-zA-Z%]+)?)')

   # Find all matches in the text
   matches = re.findall(pattern, nutrition_facts_string)

   # Create a dictionary from the matches
   nutrition_dict = {key.strip(): value.strip() for key, value in matches}


   return nutrition_dict


def parse_input(product_info):
   title = ""
   parsed = {}
   nutrition = ""

   lines = product_info.split('\n')
   title = " "
   values = set()

   if (product_info[0:5] == "https"):
      parsed["Redirect To"] = product_info
      return parsed, 1


   for i in range(len(lines)-1):
      line = lines[i]
      next_line = lines[i+1]

      line = line.strip()  # Remove leading and trailing spaces
      if(line in values):
         continue

      if line:  # Check if the line is not empty
         if (line == "Nutrition Facts"):
            parsed[line] = parse_nutrition(lines,values) 
         if not next_line:
            title = line 
            if title not in parsed:
                  parsed[title] = ""
         else:
            title = line 
            if title not in (parsed or values):
                  print(title)
                  if title in ["Ingredients", "Warnings", "Distributor", "Description", "Directions"]: # should probably keep dynamically updating 
                     parsed[title] = next_line
            values.add(next_line)
   
   parsed_final = copy.copy(parsed)

   i = 0
   for key in parsed:
      if (i > 0):
         if (parsed[key] == ''):
            parsed_final.pop(key)
      i += 1

   return parsed_final, 0 


@app.route('/uploadresults', methods =["GET", "POST"])
def uploadresults_func():
   global results, options_to_display, product_info, button_value, button_name      
   # name for product selected 

   button_value = request.form.get('button')
   if (button_value != None):
      product_info = results[button_value]
      product_info, r = parse_input(product_info)
   else:
      product_info = ""

   if (button_value in options_to_display):
      page = 2
   else:
      page = 1
   

   button_name = request.form.get('print')

   return render_template("uploadresults.html",order=order, product_name=button_value,page_num=page, product_info=product_info,buttonPressed=buttonPressed, redirect=r)
     
         
@app.route('/results', methods =["GET", "POST"])
def results_func():
   global results, options_to_display, product_info, button_value, button_name      
   # name for product selected 

   button_value = request.form.get('button')
   if (button_value != None):
      product_info = results[button_value]
      product_info, r = parse_input(product_info)
   else:
      product_info = ""

   if (button_value in options_to_display):
      page = 2
   else:
      page = 1
   

   button_name = request.form.get('print')

   return render_template("results.html",order=order, product_name=button_value,page_num=page, product_info=product_info,buttonPressed=buttonPressed, redirect=r)


# this function means print has been selected so call print fucntion here 
@app.route('/resultsprint', methods =["GET", "POST"])
def results_print():
   global results, options_to_display, product_info, button_value, button_name   
   run_backend("translation", (results[button_value]),"","","")

   if (button_value in options_to_display):
      page = 2
   else:
      page = 1

   return render_template("results.html",order=order, product_name=button_value,page_num=page, product_info=product_info,buttonPressed=buttonPressed)

# this function means upload print has been selected so call print fucntion here 
@app.route('/uploadresultsprint', methods =["GET", "POST"])
def uploadresults_print():
   global results, options_to_display, product_info, button_value, button_name   
   run_backend("translation", (results[button_value]),"","","")

   if (button_value in options_to_display):
      page = 2
   else:
      page = 1

   return render_template("uploadresults.html",order=order, product_name=button_value,page_num=page, product_info=product_info,buttonPressed=buttonPressed)

if __name__=='__main__':
   app.run(host='0.0.0.0', port=80, debug=True)


