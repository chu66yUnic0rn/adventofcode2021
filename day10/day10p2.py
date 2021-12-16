from collections import Counter
import statistics

dictionary = {")":"(", "]":"[", "}":"{", ">":"<"}
dictionary2 = {"(":")", "[":"]", "{":"}", "<":">"}
points = {")":1, "]":2, "}":3, ">":4}

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
    completion_scores = []
    for index, line in enumerate(lines):
        completion_score = 0
        opened = []
        corrupted = ""
        for char in line.strip():
            if char in ["(","[","{","<"]:
                add(opened, char)
            elif char in [")","]","}",">"]:
                is_corrupted, corrupted = is_last(opened, char)
                if is_corrupted == True:
                    break

        if corrupted == "":
            for char in reversed(opened):
                completion_score *= 5
                completion_score += points.get(dictionary2.get(char))
        if completion_score != 0:
            completion_scores.append(completion_score)
    print(statistics.median(completion_scores))
