from collections import Counter

def decode_segments(board, segments):
    print("decoding")
    decoded = 0
    combos = board.strip().split(" ")
    while decoded < 10:
        for combo in combos:
            if len(combo) == 2 and segments[1]=="":
                segments[1] = combo
                decoded += 1
                combos.remove(combo)
                print("get 1")
            elif len(combo) == 3 and segments[7]=="":
                segments[7] = combo
                decoded += 1
                combos.remove(combo)
                print("get 7")

            elif len(combo) == 4 and segments[4]=="":
                segments[4] = combo
                decoded += 1
                combos.remove(combo)
                print("get 4")

            elif len(combo) == 7 and segments[8]=="":
                segments[8] = combo
                decoded += 1
                combos.remove(combo)
                print("get 8")

            elif len(combo) == 6:
                if segments[6]!="" and segments[9]!="" and segments[0]=="":
                    segments[0] = combo
                    decoded += 1
                    combos.remove(combo)
                    print("get 0")


                if segments[1]!="" and segments[6]=="":
                    is_six = False
                    for char in segments[1]:
                        if char not in combo:
                            is_six = True
                    if is_six:
                        segments[6] = combo
                        decoded += 1
                        combos.remove(combo)
                        print("get 6")


                if segments[3]!="" and segments[8]!="" and segments[9]=="":
                    opposite_one = []
                    for char in segments[8]:
                        if char not in segments[3]:
                            opposite_one.append(char)
                    diff = 0
                    for char in opposite_one:
                        if char not in combo:
                            diff += 1
                    if diff == 1:
                        segments[9] = combo
                        decoded += 1
                        combos.remove(combo)
                        print("get 9")


            elif len(combo) == 5:
                if segments[6]!="" and segments[5]=="":
                    diff = 0
                    for char in segments[6]:
                        if char not in combo:
                            diff += 1
                    if diff == 1:
                        segments[5] = combo
                        decoded += 1
                        combos.remove(combo)
                        print("get 5")

                if segments[1]!="" and segments[3]=="":
                    is_three = True
                    for char in segments[1]:
                        if char not in combo:
                            is_three = False
                    if is_three:
                        segments[3] = combo
                        decoded += 1
                        print("get 3")

                if segments[5]!="" and segments[2]=="":
                    diff = 0
                    for char in segments[5]:
                        if char not in combo:
                            diff += 1
                    if diff == 2:
                        segments[2] = combo
                        print("get_2")
                        combos.remove(combo)
                        decoded += 1
    else:
        print(segments)


def find_match(numbers, segments):
    match = []
    for number in numbers.strip().split(" "):
        print(number)
        for index, segment in enumerate(segments):
            if Counter(number) == Counter(segment):
                print(index)
                match.append(str(index))
    return ''.join(match)


with open("day8_input") as f:
    signals = f.readlines()
    matches = []
    for signal in signals:
        segments = ["","","","","","","","","",""]
        board, numbers = signal.strip().split("|")
        decode_segments(board, segments)
        num = find_match(numbers, segments)
        matches.append(int(num))
        print(segments)
        print(matches)
        print(sum(matches))

