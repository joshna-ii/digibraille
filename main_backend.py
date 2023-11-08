from websearch import print_link, find_product
from translation import uncontracted_translation, contracted_translation, solenoid_combos

#gets information from frontend then decides what to print
#calls embossing functions
def run_backend(input_type, inp):
    if input_type == "notes":
        print_translations(inp)
        return uncontracted_translation(inp)
    elif input_type == "search":
        resp = ""
        if "https://" in inp:
            resp = print_link(inp)
        if resp == "" or resp == "error":
            return find_product(inp)
        else:
            return [{"testlink": str(resp)[:400]}, 1]
    elif input_type == "translation":
        print_translations(inp)
        
#writes translations to file for interim demo
def print_translations(inp):
    with open("temp_output.txt", "w") as f:
        f.writelines(f'Try on 172.26.17.171\n\n\n')
        f.writelines(f'PAGE TO PRINT:\n{inp}\n\n\n')
        f.writelines(f'UNCONTRACTED TRANSLATION:\n{uncontracted_translation(inp)}\n\n\n')
        f.writelines(f'CONTRACTED TRANSLATION:\n{contracted_translation(inp)}\n\n\n')
        f.writelines(f'SOLENOID INSTRUCTIONS FOR FIRST PAIR:\n{solenoid_combos(contracted_translation(inp))}')