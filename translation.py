import re
import math

#uncontract dictionaries
abcx_dict = {"a": [1,0,0,0,0,0], "b": [1,1,0,0,0,0], "c": [1,0,0,1,0,0], "d": [1,0,0,1,1,0], "e": [1,0,0,0,1,0],
                    "f": [1,1,0,1,0,0], "g": [1,1,0,1,1,0], "h": [1,1,0,0,1,0], "i": [0,1,0,1,0,0], "j": [0,1,0,1,1,0],
                    "k": [1,0,1,0,0,0], "l": [1,1,1,0,0,0], "m": [1,0,1,1,0,0], "n": [1,0,1,1,1,0], "o": [1,0,1,0,1,0],
                    "p": [1,1,1,1,0,0], "q": [1,1,1,1,1,0], "r": [1,1,1,0,1,0], "s": [0,1,1,1,0,0], "t": [0,1,1,1,1,0],
                    "u": [1,0,1,0,0,1], "v": [1,1,1,0,0,1], "w": [0,1,0,1,1,1], "x": [1,0,1,1,0,1], "y": [1,0,1,1,1,1],
                    "z": [1,0,1,0,1,1], ".": [0,1,0,0,1,1], ",": [0,1,0,0,0,0], "#": [0,0,1,1,1,1], " ": [0,0,0,0,0,0],
                    ";": [0,1,1,0,0,0], ":": [0,1,0,0,1,0], "/": [0,0,1,1,0,0], "?": [0,1,1,0,0,1], "!": [0,1,1,0,1,0],
                    "@": [0,0,1,1,1,0], "+": [0,1,1,0,1,0], "-": [0,1,0,0,1,0], "\"": [0,0,0,0,1,1], "'": [0,0,1,0,0,0],
                    "_": [0,0,0,1,1,1], "`": [0,0,0,0,1,0]}

special_dict = {"$": ([0,0,0,1,0,0],[0,1,0,0,1,1]),"%": ([0,0,0,1,0,0],[0,1,0,0,1,0],[1,1,1,1,0,0]),
                "^": ([0,0,0,1,1,1],[1,1,0,0,0,1]), "&": ([0,0,0,1,0,0],[1,1,1,1,0,1]),
                "*": ([0,0,1,0,1,0],[0,0,1,0,1,0]), "(": ([0,0,0,1,0,0],[0,1,1,0,1,1]), ")": ([0,0,0,1,0,0],[0,1,1,0,1,1]),
                "_": ([0,0,0,1,1,1],[1,1,1,0,0,0]), "{": ([0,0,0,1,0,0],[0,0,0,0,1,1],[0,1,1,0,1,1]),
                "}": ([0,0,0,1,0,0],[0,1,1,0,1,1],[0,1,1,0,0,0]), "[": ([0,0,0,1,0,0],[0,0,0,0,0,1],[0,1,1,0,1,1]),
                "]": ([0,0,0,1,0,0],[0,1,1,0,1,1],[0,0,0,0,0,1]), "|": ([0,0,0,1,1,1],[1,1,0,0,1,1]),
                "<": ([0,0,0,0,1,0],[1,0,1,0,0,0]), ">": ([0,0,0,1,0,1],[0,1,0,0,0,0]), "~": ([0,0,0,1,0,0],[1,0,0,0,1,1])}

num_dict = {"1": [1,0,0,0,0,0], "2": [1,1,0,0,0,0], "3": [1,0,0,1,0,0], "4": [1,0,0,1,1,0], "5": [1,0,0,0,1,0],
                    "6": [1,1,0,1,0,0], "7": [1,1,0,1,1,0], "8": [1,1,0,0,1,0], "9": [0,1,0,1,0,0], "0": [0,1,0,1,1,0]}

pre_num = [0,0,1,1,1,1]
after_num = [0,1,1,0,0,0] #only need if there isn't a space between number and alphabet
pre_cap = [0,0,0,0,0,1]


def uncontracted_translation(s):
    cap = False
    num = False
    trans = []
    for c in s:
        if c.isdigit():
            cap = False
            if num:
                trans.append(num_dict[c])
            else:
                trans.append(pre_num)
                trans.append(num_dict[c])
                num = True
        elif c.isupper():
            if num:
                trans.append(after_num)
            num = False
            if cap:
                trans.append(abcx_dict[c.lower()])
            else:
                trans.append(pre_cap)
                trans.append(pre_cap)
                trans.append(abcx_dict[c.lower()])
                cap = True
        elif c in abcx_dict:
            if num and c.islower():
                trans.append(after_num)
            num = False
            cap = False
            trans.append(abcx_dict[c])
        elif c in special_dict:
            num = False
            cap = False
            for e in special_dict[c]:
                trans.append(e)
    return trans


def contracted_translation(inp):  #TODO add more
    res = re.sub(r"\"", "`", inp) #conflict prevention
    #final letter groupsigns
    res = re.sub(r"ound |ound$", "kd", res)
    res = re.sub(r"ance |ance$", "ke", res)
    res = re.sub(r"sion |sion$", "kn", res)
    res = re.sub(r"less |less$", "ks", res)
    res = re.sub(r"ount |ount$", "kt", res)
    res = re.sub(r"ence |ence$", "\"e", res)
    res = re.sub(r"ong |ong$", "\"g", res)
    res = re.sub(r"ful |ful$", "\"l", res)
    res = re.sub(r"tion |tion$", "\"n", res)
    res = re.sub(r"ness |ness$", "\"s", res)
    res = re.sub(r"ment |ment$", "\"t", res)
    res = re.sub(r"ity |ity$", "\"y", res)
    #initial letter contractions
    res = re.sub(r"day |^day", "`d", res)
    #shortform words
    res = re.sub(r" about |^about | about$|^about$", "ab", res)
    return uncontracted_translation(res)



#translate arrays of 6 to arrys of 4 based on solenoid locations TODO
def solenoid_combos(inp):
    line_diff = 16 #number of lines in between pairs of solenoids
    char_per_line = 24 #number of embossed characters per line
    halfway = math.ceil((line_diff * char_per_line)/2)
    print(halfway)
    total_char = len(inp)
    instructions = []
    if total_char > halfway:
        pair1 = inp[:halfway]
        pair2 = inp[halfway:]
    else:
        pair1 = inp
        pair2 = []
    full_lines = math.floor(len(pair1)/24)
    pair2_lines = math.floor(len(pair2)/24)
    len_last_pair1 = len(pair1)%24
    len_last_pair2 = len(pair2)%24
    for i in range(full_lines):
        for j in [0,2,4]:
            for k in range(12):
                combo1 = [pair1[i*24+k][j],pair1[i*24+k+12][j]]
                combo2 = [pair1[i*24+k][j+1],pair1[i*24+k+12][j+1]]
                instructions.append(combo1)
                instructions.append(combo2)
    for j in [0,2,4]:
        for k in range(len_last_pair1):
            combo1 = [pair1[full_lines*24+k][j]]
            combo2 = [pair1[full_lines*24+k][j+1]]
            if len_last_pair1 > k+12:
                combo1.append(pair1[full_lines*24+k+12][j])
                combo2.append(pair1[full_lines*24+k+12][j+1])
            else:
                combo1.append(0)
                combo2.append(0)
            instructions.append(combo1)
            instructions.append(combo2)
    #print(f'example instructions for 1 pair: {instructions}')
    return instructions

example = [[1,0,1,0,1,0],[0,1,0,1,1,0],[1,0,1,0,1,1],[1,0,0,0,1,0],[1,1,1,0,0,1],[1,0,0,1,0,0],[1,0,1,0,1,0],[0,1,0,1,1,0],[1,0,1,0,1,1],[1,0,0,0,1,0],[1,1,1,0,0,1],[1,0,0,1,0,1]]
print(f'example braille:{example}\n\n')
solenoid_combos(example)
    