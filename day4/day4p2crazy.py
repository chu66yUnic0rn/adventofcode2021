import re
from collections import Counter
from itertools import combinations
import sys

with open("day4_input") as f:
    lines = f.readlines()
    draws = lines[0].strip().split(',')
    lines.pop(0)
    lines.pop(0)
    lines.append("\n")
    boards = []
    verticals = ["", "", "", "", ""]
    for index, line in enumerate(lines):
        if line == "\n":
            verticals = [x.strip() for x in verticals]
            boards.extend(verticals)
            verticals = ["", "", "", "", ""]
            continue
        boards.append(line.replace("  ", " ").strip())
        for i, num in enumerate(line.strip().replace("  ", " ").split(" ")):
            verticals[i] = verticals[i] + num + " "
    hits = []
    counts = 0
    for i, draw in enumerate(draws):
        for index, board in enumerate(boards):
            test_array = boards[index].split(" ")
            if draw in test_array:
                hits.append(index)
                test_array.remove(draw)
                boards[index] = " ".join(test_array)
        top_occurs = Counter(hits).most_common(10)
        print(top_occurs)
        for top_occur in top_occurs[:]:
            if top_occur[1] < 5:
                break
            else:
                top_index = top_occur[0]
                da_board = boards[top_index//10*10:top_index//10*10+10]
                if Counter(da_board) == Counter({'': 10}):
                    break
                counts += 1
                print(counts)
                if counts < len(boards)/10:
                    length_before = len(hits)
                    for x in range(top_index//10*10, top_index//10*10+10):
                        boards[x] = ''
                        while x in hits:
                            hits.remove(x)
                else:
                    top_index = Counter(hits).most_common(5)[1][0]
                    Sum = 0
                    print(draw)
                    da_board = boards[top_index//10*10:top_index//10*10+5]
                    print(da_board)
                    for board_numbers in da_board:
                        if board_numbers != "":
                            for num in board_numbers.split(" "):
                                Sum += int(num)
                    print(Sum*int(draw))
                    sys.exit(0)
