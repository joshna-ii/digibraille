from collections import OrderedDict

cache_size = 2

def create_cache():
    return OrderedDict()

def add_cache(search_input, cache, element):
    if search_input in cache:
        del cache[search_input]
    cache[search_input] = element
    if len(cache) > cache_size:
        cache.popitem(last = False)
    with open("temp_output.txt", "w") as f:
        f.writelines(f'{cache}\n\n\n')
    return cache