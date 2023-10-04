# digibraille

How to Use Right Now:
- pip install -r requirements.txt
- python3 webapp.py
    - website is 127.0.0.1:5000 (local host)

Structure of Repo:
- frontend: webapp.py and templates using python library Flask, directly interfaces with main_backend.py
- backend: main file is called main_backend.py and calls functions from the other files
    - websearch.py: handles googling, printing info from direct link, searching database for product directions
    - translation.py: converts alphabet to braille characters (set of 6 signals), converts to list of signals to be sent
    - rpi_handler.py: interfaces with rpi to host website and send signals for embosser
    - create_database.py: file that webscrapes directionsforme and other websites and outputs info into database in database_output.txt using beautifulsoup
- temporary files:
    - temp_code.py: temporary python code file for testing
    - temp_output.py: print test outputs here

Things to do:
- figure out how to host website with rpi in rpi_handler.py
- create database (dict where keywords map to webscraped info) in create_database.py
- test to see if data structure for accessing database is accessible and accurate in websearch.py
- figure out how best to convert website input html to necessary content in print_link under websearch.py
- abc to braille translations (getting book from library to learn more) in translation.py
- braille translation to embosser instructions algorithm in translation.py
- figure out how to communicate with rpi (waiting on sd card) in rpi_handler.py