from websearch import print_link, find_product
from translation import uncontracted_translation

#gets information from frontend then decides what to print
#calls embossing functions
def run_backend(search_input, notes_input): #TODO say what to print next
    if search_input == "" and notes_input == "":
        return "No input so nothing to print"
    if notes_input != "":
        str_input = f'{notes_input}' #input for translation
        print(uncontracted_translation(notes_input))
    else:
        str_input = ""
    if search_input != "":
        if str_input != "":
            str_input += "\n\n"
        resp = ""
        if "https://" in search_input:
            resp = print_link(search_input)
        if resp == "" or resp == "error":
            str_input += find_product(search_input)
        else:
            str_input += str(resp)
            print(str_input[:400])

    with open("temp_output.txt", "w") as f: #temp writing output to file
        f.writelines(f'{str_input}')