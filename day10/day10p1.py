from collections import Counter

dictionary = {")":"(", "]":"[", "}":"{", ">":"<"}
points = {")":3, "]":57, "}":1197, ">":25137}

def add(opened, char):
    opened.append(char)

def is_last(opened, char):
    if len(opened)!=0 and opened[-1] == dictionary.get(char):
        # print(opened)
        opened.pop(-1)
        return False, ""
    elif len(opened)!=0 and opened[-1] != dictionary.get(char):
        return True,char
    elif len(opened)==0:
        return False,""


with open("day10_input") as f:
    lines = f.readlines()
    syntax_error_score = 0
    for index, line in enumerate(lines):
        opened = []
        corrupted = ""
        for char in line.strip():
            if char in ["(","[","{","<"]:
                add(opened, char)
            elif char in [")","]","}",">"]:
                is_corrupted, corrupted = is_last(opened, char)
                if is_corrupted == True:
                    break
        if corrupted != "":
            syntax_error_score += points.get(corrupted)
    print(syntax_error_score)
