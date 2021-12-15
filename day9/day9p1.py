

with open("day9_input") as f:
    lines = f.readlines()
    field = [len(lines),len(lines[0].strip())]
    print(field)
    previous_low = []
    low_points = []
    for index, line in enumerate(lines):
        low = int(line[0])
        for pos, char in enumerate(line.strip()):
            if pos == 0:
                if int(char) < int(line[pos+1]):
                    previous_low.append((index,pos,int(char)))
            elif pos == field[1]-1:
                if int(char) < int(line[pos-1]):
                    previous_low.append((index,pos,int(char)))
            else:
                if int(char)<int(line[pos+1]) and int(char)<int(line[pos-1]):
                    previous_low.append((index,pos,int(char)))
    print(previous_low)

    for index,pos,low in previous_low:
        if index == 0:
            print(pos)
            number = int(lines[index+1][pos])
            if low < number:
                low_points.append(low)
        elif index == field[0]-1:
            print(pos)
            number = int(lines[index-1][pos])
            if low < number:
                low_points.append(low)
        else:
            print(pos)
            number1 = int(lines[index-1][pos])
            number2 = int(lines[index+1][pos])
            if low < number1 and low < number2:
                low_points.append(low)

    print(low_points)
    print(sum(low_points)+1*len(low_points))

