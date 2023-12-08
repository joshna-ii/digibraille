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
        elif c.isupper() and c.lower() in abcx_dict:
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
        else:
            with open("errors.txt", "w") as f:
                f.writelines(f'problem with {c}')
    return trans


def contracted_translation(inp):
    res = re.sub(r"\"", "`", inp) #conflict prevention
    #final letter groupsigns
    res = re.sub(r"ound |ound$", ">d ", res)
    res = re.sub(r"ance |ance$", "ke ", res)
    res = re.sub(r"sion |sion$", "kn ", res)
    res = re.sub(r"less |less$", "ks ", res)
    res = re.sub(r"ount |ount$", "kt ", res)
    res = re.sub(r"ence |ence$", "\"e ", res)
    res = re.sub(r"ong |ong$", "\"g ", res)
    res = re.sub(r"ful |ful$", "\"l ", res)
    res = re.sub(r"tion |tion$", "\"n ", res)
    res = re.sub(r"ness |ness$", "\"s ", res)
    res = re.sub(r"ment |ment$", "\"t ", res)
    res = re.sub(r"ity |ity$", "\"y ", res)
    #initial letter contractions
    res = re.sub(r"day", "`d", res)
    res = re.sub(r"ever", "`e", res)
    res = re.sub(r"father", "`f", res)
    res = re.sub(r"here", "`h", res)
    res = re.sub(r"know", "`k", res)
    res = re.sub(r"lord", "`l", res)
    res = re.sub(r"mother", "`m", res)
    res = re.sub(r"name", "`n", res)
    res = re.sub(r"one", "`o", res)
    res = re.sub(r"part", "`p", res)
    res = re.sub(r"question", "`q", res)
    res = re.sub(r"right", "`r", res)
    res = re.sub(r"some", "`s", res)
    res = re.sub(r"time", "`t", res)
    res = re.sub(r"under", "`u", res)
    res = re.sub(r"work", "`w", res)
    res = re.sub(r"young", "`y", res)
    #shortform words
    res = re.sub(r" about |^about | about$|^about$", " ab ", res)
    #alphabetic wordsigns
    res = re.sub(r" but |^but | but$|^but$", " b ", res)
    res = re.sub(r" can |^can | can$|^can$", " c ", res)
    res = re.sub(r" do |^do | do$|^do$", " d ", res)
    res = re.sub(r" every |^every | every$|^every$", " e ", res)
    res = re.sub(r" from |^from | from$|^from$", " f ", res)
    res = re.sub(r" go |^go | go$|^go$", " g ", res)
    res = re.sub(r" have |^have | have$|^have$", " h ", res)
    res = re.sub(r" just |^just | just$|^just$", " j ", res)
    res = re.sub(r" knowledge |^knowledge | knowledge$|^knowledge$", " k ", res)
    res = re.sub(r" like |^like | like$|^like$", " l ", res)
    res = re.sub(r" more |^more | more$|^more$", " m ", res)
    res = re.sub(r" not |^not | not$|^not$", " n ", res)
    res = re.sub(r" people |^people | people$|^people$", " p ", res)
    res = re.sub(r" quite |^quite | quite$|^quite$", " q ", res)
    res = re.sub(r" rather |^rather | rather$|^rather$", " r ", res)
    res = re.sub(r" so |^so | so$|^so$", " s ", res)
    res = re.sub(r" that |^that | that$|^that$", " t ", res)
    res = re.sub(r" us |^us | us$|^us$", " u ", res)
    res = re.sub(r" very |^very | very$|^very$", " v ", res)
    res = re.sub(r" will |^will | will$|^will$", " w ", res)
    res = re.sub(r" it |^it | it$|^it$", " x ", res)
    res = re.sub(r" you |^you | you$|^you$", " b ", res)
    res = re.sub(r" as |^as | as$|^as$", " z ", res)
    #other signs
    res = re.sub(r"st", "/", res)
    res = res.strip()
    return uncontracted_translation(res)


def pretty_print_trans(translation):
    line1 = ""
    line2 = ""
    line3 = ""
    for ch in translation:
        line1 += "  "
        line2 += "  "
        line3 += "  "
        for dot in range(0, 6):
            if dot == 0 or dot == 3:
                if ch[dot] == 0:
                    line1 += "x"
                else:
                    line1 += "o"
            elif dot == 1 or dot == 4:
                if ch[dot] == 0:
                    line2 += "x"
                else:
                    line2 += "o"
            else:
                if ch[dot] == 0:
                    line3 += "x"
                else:
                    line3 += "o"
    lines = line1 + "\n" + line2 + "\n" + line3
    return lines

#translate arrays of 6 to arrays of 2 based on solenoid locations
def solenoid_dirs(inp):
    char_diff = 3 #number of characters between solenoids
    char_per_line = 24 #number of embossed characters per line

    section_width = 2*char_diff #how many characters two solenoids emboss in a section
    sections_per_line = math.ceil(char_per_line/section_width) #number of separate sections the two solenoids emboss

    total_char = len(inp)
    total_lines = math.ceil(total_char/char_per_line)

    sol0dir = []
    sol1dir = []

    for line in range(total_lines):
        sol0_row1 = [] #dots 1 and 4 of the characters in the line
        sol0_row2 = [] #dots 2 and 5 of the characters in the line
        sol0_row3 = [] #dots 3 and 6 of the characters in the line
        sol1_row1 = [] 
        sol1_row2 = [] 
        sol1_row3 = [] 
        for col_section in range(sections_per_line):
            for character in range(char_diff):
                row = line
                col = col_section * section_width + character
                sol0x = row * char_per_line + col
                if sol0x >= total_char: #last line
                    for j in range(2):
                        sol0_row1.append(0)
                        sol0_row2.append(0)
                        sol0_row3.append(0)
                        sol1_row1.append(0)
                        sol1_row2.append(0)
                        sol1_row3.append(0)
                else:
                    for combo in range(2): #if row 1, dots 1 then 4 and so on
                        #solenoid 1
                        sol0_row1.append(inp[sol0x][0+3*combo])
                        sol0_row2.append(inp[sol0x][1+3*combo])
                        sol0_row3.append(inp[sol0x][2+3*combo])
                        #solenoid 2
                        sol1x = sol0x+char_diff
                        if sol1x < total_char:
                            sol1_row1.append(inp[sol0x+char_diff][0+3*combo])
                            sol1_row2.append(inp[sol0x+char_diff][1+3*combo])
                            sol1_row3.append(inp[sol0x+char_diff][2+3*combo])
                        else:
                            sol1_row1.append(0)
                            sol1_row2.append(0)
                            sol1_row3.append(0)
        sol0_row1.reverse()
        sol0_row2.reverse()
        sol0_row3.reverse()
        sol1_row1.reverse()
        sol1_row2.reverse()
        sol1_row3.reverse()
        sol0dir += sol0_row1 + sol0_row2 + sol0_row3
        sol1dir += sol1_row1 + sol1_row2 + sol1_row3

    instructions = [sol0dir, sol1dir]
    return instructions

    

def solenoid_combos(solenoidDirs):
    sol0dirs = solenoidDirs[0] #top left sol
    sol1dirs = solenoidDirs[1] #top right sol
    length = len(sol0dirs) #all should be the same length
    sol_combos = ""
    for i in range(length):
        binary_combo = str(sol1dirs[i]) + str(sol0dirs[i])
        sol_combos += (str(int(binary_combo,2))) + " "
    return(sol_combos)