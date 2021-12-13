from collections import Counter

def get_fish(pool, days):
    for i in range(days):
        print("day" + str(i+1))
        for index, time in enumerate(pool[:]):
            pool[index] = str(int(time)-1)
            if pool[index] == '-1':
                pool[index] = '6'
                pool.append('8')
    return pool

with open("day6_input") as f:
    original_pool = f.read().strip().split(",")
    print(original_pool)
    middle_pool = []
    for each_fish in original_pool:
        middle_pool.extend(get_fish([each_fish], 100))

    c = Counter(middle_pool)
    new_pool = list(c.keys())
    final_length = 0
    for each_fish in new_pool:
        final_length += len(get_fish([each_fish], 156))*c.get(each_fish)
    
    print(final_length)

