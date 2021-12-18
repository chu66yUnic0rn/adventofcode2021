from operator import itemgetter
from collections import Counter

with open("day13_input") as f:
    lines = f.readlines()
    dots = []
    instructions = []
    for line in lines:
        if "," in line:
            x,y = line.strip().split(",")
            dots.append((int(x),int(y)))
        if "=" in line:
            instruction = line.strip().split(" ")[-1]
            coord,num = instruction.split("=")
            instructions.append((coord,int(num)))

    for i in range(1):
        print(dots)
        coord,num = instructions[i]
        if coord == "x":
            for index,(x,y) in enumerate(dots):
                if x > num:
                    x = x-num-1
                    dots[index] = (x,y)
                elif x < num:
                    x = abs(num-x)-1
                    dots[index] = (x,y)
        if coord == "y":
            for index,(x,y) in enumerate(dots):
                if y > num:
                    y = num-abs(y-num)
                    dots[index] = (x,y)
    #print(dots)
    print(list(Counter(dots)))
    print(len(list(Counter(dots))))
                





