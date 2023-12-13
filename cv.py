import cv2
from pyzbar.pyzbar import decode #brew install zbar
import pytesseract
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
from barcode_database import check_database, write_to_csv

def run_cv(image):
   resd = OrderedDict()
   barcode = read_barcode(image)
   if barcode == "NA":
      resd = image_to_text(image)
      return [resd, "Barcode Not Detected"]
   else:
      [title, directions] = check_database(barcode)
      if title == "NA":
         [title, directions] = search_barcode(barcode)
         write_to_csv(barcode, title, directions)
      resd[title] = directions
      return [resd, "Barcode Detected"]
   

def read_barcode(image):  
    img = cv2.imread(image)
    detectedBarcodes = decode(img)
      
    # check if barcode detected
    if not detectedBarcodes:
      return "NA"
    else:
      return detectedBarcodes[0].data.decode("ascii")
    

def search_barcode(barcode):
   URL = f"https://go-upc.com/search?q={barcode}"
   r = requests.get(URL)
   soup = BeautifulSoup(r.content, 'html5lib')
   title = soup.find("title").text
   description = soup.find("span")
   if description == None:
      description = ""
   else:
      description = description.text
   directions = title + "\n\n\n" + "Description" + "\n" + description.strip()
   return [title, directions]



def image_to_text(image):
    resd = OrderedDict()

    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
    img = cv2.imread(image)
    
    #using cv functions to process before reading
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
    dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                    cv2.CHAIN_APPROX_NONE)
    # Creating a copy of image
    im2 = img.copy()
    directions = ""
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)
        directions += f"{text}\n"
    resd["No Barcode Detected: Click for Image Text"] = directions
    return resd