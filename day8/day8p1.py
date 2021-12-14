def find_match(numbers):
    match = 0
    for number in numbers.strip().split(" "):
        if len(number) in [2,3,4,7]:
            match += 1
    return match

with open("day8_input") as f:
    signals = f.readlines()
    matches = 0
    for signal in signals:
        board, numbers = signal.strip().split("|")
        matches += find_match(numbers)
    print(matches)

