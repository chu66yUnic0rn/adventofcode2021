def land_in_target(initial, x_value, y_value):
    x_min = int(x_value.split(".")[0])
    x_max = int(x_value.split(".")[2])
    y_min = int(y_value.split(".")[0])
    y_max = int(y_value.split(".")[2])
    x_velocity, y_velocity = initial
    x_pos, y_pos = (0,0)
    y_marks = []
    while x_pos <= x_max and y_pos >= y_min:
        y_marks.append(y_pos)
        if x_min <= x_pos <= x_max and y_min <= y_pos <= y_max:
            return True
        if x_velocity > 0:
            x_pos += x_velocity
            x_velocity -= 1
        elif x_velocity < 0:
            x_pos += x_velocity
            x_velocity += 1
        y_pos += y_velocity
        y_velocity -=1
    else:
        return False


with open("day17_input") as f:
    parts = f.read().strip().split(" ")
    x_value = parts[2].strip(',').split("=")[1]
    y_value = parts[3].split("=")[1]
    print(x_value, y_value)

    good_landing = []

    for x in range(0,100):
        for y in range(-600, 600):
            result = land_in_target((x,y), x_value, y_value)
            if result == True:
                good_landing.append((x,y))
    print(len(good_landing))

    
