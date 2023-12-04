from websearch import find_product_database, find_product_query
from translation import uncontracted_translation, contracted_translation, solenoid_dirs, solenoid_combos, pretty_print_trans
from cache import search_cache
#from gpio_button import check_grade
#from rpi_handler import send_solenoids

grade = "contracted"

#writes translations to file for demo
def print_translations(grade, inp, uncontracted, contracted, sol_dirs, sol_combos, pretty_print):
    with open("backend_translations.txt", "w") as f:
        f.writelines(f'PAGE TO PRINT:\n{inp}\n\n\n')
        f.writelines(f'UNCONTRACTED TRANSLATION:\n{uncontracted}\n\n\n')
        f.writelines(f'CONTRACTED TRANSLATION:\n{contracted}\n\n\n')
        if len(uncontracted) < 10:
            f.writelines(f'BRAILLE SIMULATION:\n{pretty_print}\n\n\n')
        f.writelines(f'SOLENOID INSTRUCTIONS for {grade.upper()} BRAILLE:\n{sol_dirs}\n\n\n')
        f.writelines(f'ARDUINO COMBOS:\n{sol_combos}\n\n\n')

#gets information from frontend then decides what to print
#calls embossing functions
def run_backend(input_type, inp, db_for_search, database_or_query, cache):
    global grade
    if input_type == "notes" or input_type == "translation":
        uncontracted = uncontracted_translation(inp)
        contracted = contracted_translation(inp)
        #grade = check_grade()
        if grade == "uncontracted":
            sol_dirs = solenoid_dirs(uncontracted)
            pretty_print = pretty_print_trans(uncontracted)
        else:
            sol_dirs = solenoid_dirs(contracted)
            pretty_print = pretty_print_trans(contracted)
        sol_combos = solenoid_combos(sol_dirs)
     #   send_solenoids(sol_combos) TODO
        print_translations(grade, inp, uncontracted, contracted, sol_dirs, sol_combos, pretty_print)
        return uncontracted_translation(inp)
    elif input_type == "search":
        if inp in cache:
            return search_cache(cache, inp)
        else:
            if database_or_query == "db":
                return find_product_database(inp, db_for_search)
            elif database_or_query == "query":
                return find_product_query(inp)