#uncontract dictionaries
abcx_dict = {"a": [1,0,0,0,0,0], "b": [1,1,0,0,0,0], "c": [1,0,0,1,0,0], "d": [1,0,0,1,1,0], "e": [1,0,0,0,1,0],
                    "f": [1,1,0,1,0,0], "g": [1,1,0,1,1,0], "h": [1,1,0,0,1,0], "i": [0,1,0,1,0,0], "j": [0,1,0,1,1,0],
                    "k": [1,0,1,0,0,0], "l": [1,1,1,0,0,0], "m": [1,0,1,1,0,0], "n": [1,0,1,1,1,0], "o": [1,0,1,0,1,0],
                    "p": [1,1,1,1,0,0], "q": [1,1,1,1,1,0], "r": [1,1,1,0,1,0], "s": [0,1,1,1,0,0], "t": [0,1,1,1,1,0],
                    "u": [1,0,1,0,0,1], "v": [1,1,1,0,0,1], "w": [0,1,0,1,1,1], "x": [1,0,1,1,0,1], "y": [1,0,1,1,1,1],
                    "z": [1,0,1,0,1,1], ".": [0,1,0,0,1,1], ",": [0,1,0,0,0,0], "#": [0,0,1,1,1,1], " ": [0,0,0,0,0,0],
                    ";": [0,1,1,0,0,0], ":": [0,1,0,0,1,0], "/": [0,0,1,1,0,0], "?": [0,1,1,0,0,1], "!": [0,1,1,0,1,0],
                    "@": [0,0,1,1,1,0], "+": [0,1,1,0,1,0], "-": [0,1,0,0,1,0], "\"": [0,0,0,0,1,0], "'": [0,0,1,0,0,0],
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

#create uncontracted braille function TODO
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



#contracted braille TODO
#try for AB, AB CD, AbC, AB12CD, ab AB, AB cd
#nested loop or separate loop?
#brackets/parentheses



#translate arrays of 6 to arrys of 4 based on solenoid locations