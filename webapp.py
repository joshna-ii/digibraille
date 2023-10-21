# importing Flask and other modules
from flask import Flask, request, render_template
#from main_backend import run_backend
 
# Flask constructor
app = Flask(__name__)  
 

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def gfg():
   return render_template("website.html")

# function for typing notes feature on web app
@app.route('/typenotes', methods =["GET", "POST"])
def typenotes():
   if request.method == "POST":
      # getting input with notes in HTML form
      notes_input = request.form.get("notes")
      #run_backend(search_input, notes_input) #from websearch.py REMEMBER TO UNCOMMENT WHEN DONE
      return f'printing now:\n{notes_input}' #TODO find way to have a back and forth for product searching
   return render_template("typenotes.html")


# function for searching product feature on webapp
@app.route('/searchproduct')
def searchproduct():
   if request.method == "POST":
      # getting input with search in HTML form
      search_input = request.form.get("search")
      # getting input with notes in HTML form
      #run_backend(search_input, notes_input) #from websearch.py REMEMBER TO UNCOMMENT WHEN DONE
      return f'printing now:\n{search_input}' #TODO find way to have a back and forth for product searching
      # return run back-end 
   return render_template("searchproduct.html")


 
if __name__=='__main__':
   app.run()




