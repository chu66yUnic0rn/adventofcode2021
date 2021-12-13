from collections import Counter

def valid_coord(line):
    components = line.strip().split(" ")
    start = components[0]
    end = components[2]
    start_coord = start.split(",")
    end_coord = end.split(",")
    valid = []
    if start_coord[0] == end_coord[0]:
        smaller, bigger,_ = get_range(start_coord[1], end_coord[1])
        for y in range(smaller, bigger):
            valid.append(','.join([start_coord[0],str(y)]))
        print(valid)
    elif start_coord[1] == end_coord[1]:
        smaller, bigger,_ = get_range(start_coord[0], end_coord[0])
        for x in range(smaller, bigger):
            valid.append(','.join([str(x),start_coord[1]]))
        print(valid)
    else:
        _,_,steps = get_range(start_coord[0], end_coord[0])
        start_x = int(start_coord[0])
        start_y = int(start_coord[1])
        end_x = int(end_coord[0])
        end_y = int(end_coord[1])
        if start_x < end_x and start_y < end_y:
            for i in range(steps):
                point_x = start_x+i
                point_y = start_y+i
                valid.append(','.join([str(point_x), str(point_y)]))
        if start_x > end_x and start_y > end_y:
            for i in range(steps):
                point_x = start_x-i
                point_y = start_y-i
                valid.append(','.join([str(point_x), str(point_y)]))
        if start_x < end_x and start_y > end_y:
            for i in range(steps):
                point_x = start_x+i
                point_y = start_y-i
                valid.append(','.join([str(point_x), str(point_y)]))
        if start_x > end_x and start_y < end_y:
            for i in range(steps):
                point_x = start_x-i
                point_y = start_y+i
                valid.append(','.join([str(point_x), str(point_y)]))
        print(valid)
    return valid

def get_range(num1, num2):
    smaller = min(int(num1), int(num2))
    bigger = max(int(num1)+1, int(num2)+1)
    return smaller, bigger, bigger-smaller

with open("day5_input") as f:
    lines = f.readlines()
    print(lines)
    valid_coords = []
    for line in lines:
        new_points = valid_coord(line)
        if new_points:
            valid_coords.extend(new_points)
    count = 0
    for point in Counter(valid_coords).most_common():
        if point[1] > 1:
            count += 1
    print(Counter(valid_coords))
    print(count)

