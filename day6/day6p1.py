def get_fish(pool, days):
    for i in range(days):
        pool.sort()
        print("day" + str(i+1))
        for index, time in enumerate(pool[:]):
            pool[index] = str(int(time)-1)
            if pool[index] == '-1':
                pool[index] = '6'
                pool.append('8')
        #print(pool)
    return pool

with open("day6_input") as f:
    original_pool = f.read().strip().split(",")
    print(original_pool)
    new_pool = get_fish(original_pool, 80)
    print(len(new_pool))

