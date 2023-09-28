# importing Flask and other modules
from flask import Flask, request, render_template
import requests
from websearch import *
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
   if request.method == "POST":
      # getting input with search in HTML form
      search_input = request.form.get("search")
      # getting input with notes in HTML form
      notes_input = request.form.get("notes")
      if search_input == "": #no search input
         if notes_input == "": #no notes input
            return "No input so nothing to print"
         else: #just notes input
            return "printing now: " + notes_input
      else:
         search(search_input) #function from websearch
         if notes_input == "": #just search input
            return "printing now: " + search_input
         else: #both search and notes niput
            return "printing now: " + search_input + " and " + notes_input
      return "other"
   return render_template("website.html")

 
if __name__=='__main__':
   app.run()