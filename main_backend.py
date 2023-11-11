from websearch import print_link, find_product
from translation import uncontracted_translation

#gets information from frontend then decides what to print
#calls embossing functions
def run_backend(input_type, inp):
    if input_type == "notes":
        return uncontracted_translation(inp)
    elif input_type == "search":
        resp = ""
        if "https://" in inp:
            resp = print_link(inp)
        if resp == "" or resp == "error":
            return find_product(inp)
        else:
            return [{"testlink": str(resp)[:400]}, 1]

    #with open("temp_output.txt", "w") as f: #temp writing output to file TODO delete
    #    f.writelines(f'{str_input}')