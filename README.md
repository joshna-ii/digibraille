# digibraille

How to Use Right Now:
- pip install -r requirements.txt
- python3 webapp.py or sudo python3 webapp.py on raspberry pi
    - website is ip address of host device: hostname -I in command terminal to find ip address

Structure of Repo:
- frontend: webapp.py and templates using python library Flask, directly interfaces with main_backend.py
- backend: main file is called main_backend.py and calls functions from the other files
    - websearch.py: handles googling, printing info from direct link, searching database for product directions
    - translation.py: uses dict to convert alphabet to braille characters (list of 6 0/1s) for uncontracted braille, loops through again for uncontracted braille, converts to list of location and solenoid movement to be sent
    - rpi_handler.py: interfaces with rpi to send signal to arduino for embosser
    - create_database.py: file that webscrapes directionsforme and other websites and outputs info into database using beautifulsoup
    - databasexxxx.csv: database output
    - demo.ino: arduino file that is run on the arduino and interacts with rpi_handler.py over serial
- temporary files:
    - temp_code.py: temporary python code file for testing
    - temp_output.py: print temporary test outputs here

Things to do:
- use rc.local to immediately run webapp.py when rpi is plugged in (headless)
- webscrape backofthebox.com then create database with it
- stress unit tests
- computer vision for printing box instructions
- rpi to arduino to stepper motor pipeline
- work on cache system for most recent searches
- make button for normal vs. jumbo size and grade 1 vs. grade 2 vs. grade 3