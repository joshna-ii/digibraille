# importing Flask and other modules
<<<<<<< HEAD
from flask import Flask, request, render_template, jsonify
from websearch import print_link, find_product
import copy
#from main_backend import run_backend
=======
from flask import Flask, request, render_template
import copy
from main_backend import run_backend
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
 
# Flask constructor
app = Flask(__name__)  
 
# global results 
results  = []
options_to_display = {}
n = 0
search_input = ""
buttonPressed = False
product_info = {}
button_value = ""
button_name = ""

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

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def gfg():
   return render_template("website.html")

# function for typing notes feature on web app
@app.route('/typenotes', methods =["GET", "POST"])
def typenotes():
   if request.path == '/typenotes':
      if request.method == "POST":
         # getting input with notes in HTML form
         notes_input = request.form.get("notes")
<<<<<<< HEAD
         #run_backend(search_input, notes_input) #from websearch.py REMEMBER TO UNCOMMENT WHEN DONE
        #return f'printing now:\n{notes_input}' #TODO find way to have a back and forth for product searching
=======
         run_backend("notes", notes_input)
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
   return render_template("typenotes.html")


# function for searching product feature on webapp
@app.route('/searchproduct', methods =["GET", "POST"])
def searchproduct(page=0):
   global results,n, search_input  
   if request.path == '/searchproduct':
      if request.method == "POST":

         # getting input with search in HTML form
         search_input = request.form.get("search")
<<<<<<< HEAD
         # getting input with notes in HTML form
         #run_backend(search_input, notes_input) #from websearch.py REMEMBER TO UNCOMMENT WHEN DONE
         [results,n] = find_product(search_input)
=======
         [results,n] = run_backend("search", search_input)
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41

         items_per_page = 5
         start_index = page*items_per_page + 0 
         end_index = page*items_per_page + 5
         options_to_display = {}
         c = 0 

         for key in results:
            if ( c >= start_index and c < end_index):
               options_to_display[key] = results[key]
            c += 1 

<<<<<<< HEAD
        # results = results.splitlines()
         search_performed = bool(results)
         return render_template("searchproduct.html",results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)#TODO find way to have a back and forth for product searching
         # return run back-end 
=======
         search_performed = bool(results)
         return render_template("searchproduct.html",results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41

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
<<<<<<< HEAD
      return render_template("searchproduct.html",results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)#TODO find way to have a back and forth for product searching
=======
      return render_template("searchproduct.html",results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41



# function for searching product feature on webapp
@app.route('/nextpage', methods =["GET", "POST"])
def nextpage(results=results):
   global search_input, options_to_display
   page = 1
   if request.path == '/nextpage':
         # getting input with search in HTML form
         if request.method == "POST":
            search_input = request.form.get("search")
<<<<<<< HEAD
         # getting input with notes in HTML form
         #run_backend(search_input, notes_input) #from websearch.py REMEMBER TO UNCOMMENT WHEN DONE
         [results,n] = find_product(search_input)
=======
         [results,n] = run_backend("search", search_input)
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41

         items_per_page = 5
         start_index = page*items_per_page + 0 
         end_index = page*items_per_page + 5
         options_to_display = {}
         c = 0 

         for key in results:
            if ( c >= start_index and c < end_index):
               options_to_display[key] = results[key]
            c += 1 

<<<<<<< HEAD
         
        # results = results.splitlines()
         search_performed = bool(results)
         return render_template("nextpage.html",results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)#TODO find way to have a back and forth for product searching
         # return run back-end 
       #  if ( request.method == "POST"): DO SOMETHING IF USER WANTS TO SEARCH AGAIN ON SAME PAGE
=======
         search_performed = bool(results)
         return render_template("nextpage.html",results=options_to_display,num=n,search_input=search_input,search_performed=search_performed,current_page=page)
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41

   return render_template("nextpage.html",current_page=page,search_input=search_input)

def parse_nutrition(lines,values):
<<<<<<< HEAD
   
=======
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
   i = 0
   hit = 0
   nutrition = ""
   nut_dict = {}

   for line in lines:
      values.add(line)
      if (line == "Nutritional Facts"):
         hit = 1 
      if (hit == 1 and line):
         if (line != "Nutritional Facts"):
            nutrition += line + """
"""
      if (hit == 1 and line == ''):
         break
   
   nutr_lines = nutrition.split('\n')
   for line in nutr_lines:
      if line:
         new_line = line.split(":")
         for i in range(len(new_line)):  
            new_line[i] = new_line[i].strip()

         nut_dict[new_line[0]] = new_line[1]
      
   return nut_dict


def parse_input(product_info):
   title = ""
   parsed = {}
   nutrition = ""

   lines = product_info.split('\n')
   title = " "
   values = set()


   for i in range(len(lines)-1):
      line = lines[i]
      next_line = lines[i+1]

      
      line = line.strip()  # Remove leading and trailing spaces
      if(line in values):
         continue

      if line:  # Check if the line is not empty
         if (line == "Nutritional Facts"):
            parsed[line] = parse_nutrition(lines,values) 
         if not next_line:
            title = line 
            if title not in parsed:
                  parsed[title] = ""
         else:
            title = line 
            if title not in parsed and values:
               parsed[title] = next_line
            values.add(next_line)
   
   parsed_final = copy.copy(parsed)

   i = 0
   for key in parsed:
      if (i > 0):
         if (parsed[key] == ''):
            parsed_final.pop(key)
      i += 1

   return parsed_final 
     
         
@app.route('/results', methods =["GET", "POST"])
def results_func():
   global results, options_to_display, product_info, button_value, button_name      
<<<<<<< HEAD

   # name for product selected 
   button_value = request.form.get('button')
   notes_input = ""

=======
   # name for product selected 
   button_value = request.form.get('button')
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
   if (button_value != None):
      product_info = results[button_value]
      product_info = parse_input(product_info)
   else:
      product_info = ""

<<<<<<< HEAD

=======
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
   if (button_value in options_to_display):
      page = 2
   else:
      page = 1
<<<<<<< HEAD

   
   button_name = request.form.get('print')



=======
   
   button_name = request.form.get('print')

>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
   return render_template("results.html",product_name=button_value,page_num=page, product_info=product_info,buttonPressed=buttonPressed)


# this function means print has been selected so call print fucntion here 
@app.route('/resultsprint', methods =["GET", "POST"])
def results_print():
   global results, options_to_display, product_info, button_value, button_name      
<<<<<<< HEAD

   print("here")
   
=======
   run_backend("translation", (results[button_value]))
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41

   if (button_value in options_to_display):
      page = 2
   else:
      page = 1

<<<<<<< HEAD



=======
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41
   return render_template("results.html",product_name=button_value,page_num=page, product_info=product_info,buttonPressed=buttonPressed)


if __name__=='__main__':
<<<<<<< HEAD
   app.run(host='0.0.0.0', port=80,debug=True)
=======
   app.run(host='0.0.0.0', port=80, debug=True)
>>>>>>> bc01dcb3cb579b96d844c063d53891a779ddee41




