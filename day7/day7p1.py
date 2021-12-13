from collections import Counter
import statistics

def find_median(crab_pool):
    if len(crab_pool)%2 == 1:
        return statistics.median(crab_pool), None
    #crab_pool[len(crab_pool)//2]
    else:
        median1 = statistics.median_low(crab_pool)
        median2 = statistics.median_high(crab_pool)
        print(median1, median2)
        return str(median1), str(median2) 

def find_mode(crab_pool):
    print(statistics.mode(crab_pool))
    return statistics.mode(crab_pool)

def find_average(crab_pool):
    total = 0
    for crab in crab_pool:
        total += int(crab)
    return(str(total//len(crab_pool)))

def calculate_fuel(crab_pool, position):
    fuel = 0
    for crab in crab_pool:
        fuel += abs(int(crab),int(position))
        steps = abs(int(crab)-int(position))
        cost = (1+steps)*steps//2
        fuel += cost
    return fuel

with open("day7_testinput") as f:
    crab_pool = f.read().strip().split(",")
    median1, median2 = find_median(crab_pool)
    print(median1, median2)
    mode = find_mode(crab_pool)
    print(mode)
    average = find_average(crab_pool)
    print(average)
    median1_fuel = calculate_fuel(crab_pool, median1)
    if median2 is not None:
        median2_fuel = calculate_fuel(crab_pool,median2)
    else:
        median2_fuel = None
    mode_fuel = calculate_fuel(crab_pool, mode)
    average_fuel = calculate_fuel(crab_pool, average)
    print(median1_fuel, median2_fuel)
    print(mode_fuel)
    print(average_fuel)
    
    if median2_fuel is not None:
        print(min(median1_fuel, median2_fuel, mode_fuel, average_fuel))
    else:
        print(min(median1_fuel, mode_fuel, average_fuel))
