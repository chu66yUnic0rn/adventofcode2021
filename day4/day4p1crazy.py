import re
from collections import Counter
from itertools import combinations

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
    print(len(boards))
    hits = []
    for i, draw in enumerate(draws):
        if draw in draws[:i]:
            print(draw, draws[:i])
            continue
        for index, board in enumerate(boards):
            test_array = boards[index].split(" ")
            if draw in test_array:
                hits.append(index)
                test_array.remove(draw)
                boards[index] = " ".join(test_array)
                print(boards[index])

        top_occur = Counter(hits).most_common(1)

        if top_occur[0][1] == 5:
            top_index = top_occur[0][0]
            print(draw)
            print(boards[top_index])
            da_board = boards[top_index//10*10:top_index//10*10+5]
            print(da_board)
            Sum = 0
            for board_numbers in da_board:
                if board_numbers != "":
                    for num in board_numbers.split(" "):
                        Sum += int(num)

            print(Sum*int(draw))
            break


