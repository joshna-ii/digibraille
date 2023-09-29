# importing Flask and other modules
from flask import Flask, request, render_template
from main_backend import run_backend
 
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
      run_backend(search_input, notes_input) #from websearch.py
      return f'printing now:\n{search_input}\n{notes_input}' #TODO find way to have a back and forth for product searching
   return render_template("website.html")

 
if __name__=='__main__':
   app.run()