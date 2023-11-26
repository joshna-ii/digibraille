from websearch import print_link, find_product_database
from queries import find_product_query
from translation import uncontracted_translation, contracted_translation, solenoid_dirs, solenoid_combos
#from rpi_handler import send_solenoids


#writes translations to file for interim demo
def print_translations(inp, uncontracted, contracted, sol_dirs, sol_combos):
    with open("temp_output.txt", "w") as f:
        f.writelines(f'Try on 172.26.17.171\n\n\n')
        f.writelines(f'PAGE TO PRINT:\n{inp}\n\n\n')
        f.writelines(f'UNCONTRACTED TRANSLATION:\n{uncontracted}\n\n\n')
        f.writelines(f'CONTRACTED TRANSLATION:\n{contracted}\n\n\n')
        f.writelines(f'SOLENOID INSTRUCTIONS:\n{sol_dirs}\n\n\n')
        f.writelines(f'ARDUINO COMBOS:\n{sol_combos}\n\n\n')

#gets information from frontend then decides what to print
#calls embossing functions
def run_backend(input_type, inp, db_for_search, database_or_query):
    if input_type == "notes":
        uncontracted = uncontracted_translation(inp)
        contracted = contracted_translation(inp)
        sol_dirs = solenoid_dirs(contracted)
        sol_combos = solenoid_combos(sol_dirs)
     #   send_solenoids(sol_combos)
        print_translations(inp, uncontracted, contracted, sol_dirs, sol_combos)
        return uncontracted_translation(inp)
    elif input_type == "search":
        resp = ""
        if "https://" in inp:
            resp = print_link(inp)
        if resp == "" or resp == "error":
            if database_or_query == "db":
                return find_product_database(inp, db_for_search)
            else:
                return find_product_query(inp)
        else:
            return [{"testlink": str(resp)[:400]}, 1]
    elif input_type == "translation":
        uncontracted = uncontracted_translation(inp)
        contracted = contracted_translation(inp)
        sol_dirs = solenoid_dirs(contracted)
        sol_combos = solenoid_combos(sol_dirs)
        #send_solenoids(sol_combos) TODO
        print_translations(inp, uncontracted, contracted, sol_dirs, sol_combos)