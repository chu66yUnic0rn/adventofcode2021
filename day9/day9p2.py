

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
            # print(pos)
            number = int(lines[index+1][pos])
            if low < number:
                low_points.append((index,pos))
        elif index == field[0]-1:
            # print(pos)
            number = int(lines[index-1][pos])
            if low < number:
                low_points.append((index,pos))
        else:
            # print(pos)
            number1 = int(lines[index-1][pos])
            number2 = int(lines[index+1][pos])
            if low < number1 and low < number2:
                low_points.append((index,pos))

    print(low_points)
    basins = []
    for low_point in low_points:
        queue = [low_point]
        basin = []
        while len(queue) != 0:
        # for _ in range(3):
            index, pos = queue[0]
            if index > 0:
                if lines[index-1][pos]!='9' and (index-1,pos) not in basin:
                    queue.append((index-1,pos))

            if pos > 0:
                if lines[index][pos-1]!='9' and (index, pos-1) not in basin:
                    queue.append((index, pos-1))
            if pos < field[1]-1:
                if lines[index][pos+1]!='9' and (index, pos+1) not in basin:
                    queue.append((index, pos+1))
            if index < field[0]-1:
                if lines[index+1][pos]!='9' and (index+1,pos) not in basin:
                    queue.append((index+1,pos))

            new = queue.pop(0)
            if new not in basin:
                basin.append(new)
            # print(queue)
            # print(basin)
        else:
            basins.append(basin)
    print(basins.sort(key=len,reverse=True))
    total = 1
    for i in range(3):
        total *= len(basins[i])
    print(total)

                    



