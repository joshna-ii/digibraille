import csv

def write_to_csv(barcode, title, directions):
    with open(f'database.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([barcode, title, directions])

def check_database(barcode):
    with open(f'database.csv', 'r', newline='\n') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if barcode == row[0]:
                return [row[1], row[2]]
        return ["NA", "NA"]
    
def reset_database():
    with open(f'database.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(["barcode", "title", "directions"])