# digibraille

How to Use Right Now:
pip install -r requirements.txt
python3 webapp.py
- website is 127.0.0.1:5000 (local host)
- just prints some info to browser and local terminal rn based on input

Structure of Repo:
- frontend: webapp.py and templates using python library Flask, directly interfaces with main_backend.py
- backend: main file is called main_backend.py and calls functions from the other files
    websearch.py: handles googling, printing info from direct link, webscraping for product directions
    translation.py: converts alphabet to braille characters (set of 6 signals), converts to list of signals to be sent
    rpi_handler.py: interfaces with rpi to host website and send signals for embosser
- temporary files:
    temp_code.py: code for finding product directions
    temp_output.py: print test outputs here

Thoughts on Improvement:
- might need to have internal database because webscraping is taking too long and use google if not in internal database

Things to do:
- figure out how to host with rpi
- figure out how to find relevant website
- figure out how best to convert website html to necessary content
- abc to braille translations
- braille translation to embosser instructions
- figure out how to communicate with rpi
- improve frontend interface to make accessible and clean