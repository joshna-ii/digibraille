import cv2
from pyzbar.pyzbar import decode #brew install zbar
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup

def run_cv(image):
   barcode = read_barcode(image)
   if barcode == "NA":
      return [OrderedDict(), 0]
   else:
      return search_barcode(barcode)

def read_barcode(image):  
    img = cv2.imread(image)
    detectedBarcodes = decode(img)
      
    # check if barcode detected
    if not detectedBarcodes:
      return "NA"
    else:
      return detectedBarcodes[0].data.decode("ascii")
    
def search_barcode(barcode):
   resd = OrderedDict()
   count = 1
   URL = f"https://go-upc.com/search?q={barcode}"
   r = requests.get(URL)
   soup = BeautifulSoup(r.content, 'html5lib')
   title = soup.find("title").text
   description = soup.find("span").text
   directions = title + "\n\n\n" + "Description" + "\n" + description.strip()
   resd[title] = directions
   return [resd, count]