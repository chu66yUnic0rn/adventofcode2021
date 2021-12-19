def find_next(index, pos, last_i, last_p):
    paths = []
    if index < last_i:
        paths.append((index+1, pos))
    if 0 < index:
        paths.append((index-1,pos))
    if pos < last_p:
        paths.append((index,pos+1))
    if 0 < pos:
        paths.append((index, pos-1))
    return paths

with open("day15_input") as f:
    lines = f.readlines()
    da_map = {}
    last_one = []
    for index, line in enumerate(lines):
        for pos, char in enumerate(line.strip()):
            da_map.update({(index, pos): int(char)})

    currents = {(0,0):0}
    #while (len(lines)-1, len(lines[0].strip())-1) not in currents.keys():
    for _ in range(200):
        steps = {}
        for current, score in currents.items():
            index, pos = current
            results = find_next(index, pos, len(lines)-1, len(lines[0].strip())-1)
            for result in results:
                if steps.get(result) is None:
                    steps.update({result:score+da_map[result]})
                if steps.get(result) > score+da_map[result]:
                    steps.update({result:score+da_map[result]})

        print(steps)
        currents = steps
        if currents.get((len(lines)-1, len(lines[0].strip())-1)):
            last_one.append(currents.get((len(lines)-1, len(lines[0].strip())-1)))
    print(min(last_one))





    

