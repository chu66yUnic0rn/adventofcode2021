def forward(coordinate, value):
    coordinate[0] += int(value)
    coordinate[1] += int(value)*coordinate[2]
    return coordinate

def down(coordinate, value):
    coordinate[2] += int(value)
    return coordinate

def up(coordinate, value):
    coordinate[2] -= int(value)
    return coordinate if coordinate[2]>0 else [coordinate[0],coordinate[1],0]

def get_instruction(coordinate,line):
    command, value = line.strip().split()
    print(command, value)
    if command == "forward":
        return forward(coordinate, value)
    if command == "down":
        return down(coordinate, value)
    if command == "up":
        return up(coordinate, value)
    return coordinate

with open('day2_input') as f:
    instructions = f.readlines()
    #print(instructions)
    now = [0,0,0]
    #now = up(forward(begin, 2), 1)
    for ins in instructions:
        now = get_instruction(now, ins)
        print(now)
    print(now)
    print(now[0]*now[1])

