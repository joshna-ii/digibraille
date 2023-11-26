from translation import uncontracted_translation
import string
import random


def uncontracted_translation_test():
    # initializing size of string
    N = 7
 
    # generating random strings
    res = ''.join(random.choices((string.ascii_letters + string.digits + string.punctuation), k=N))
 
    # print result
    print("The generated random string : " + str(res))

    trans = uncontracted_translation(res)
    print(trans)