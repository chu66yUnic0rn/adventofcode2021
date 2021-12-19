from collections import Counter

with open("day14_input") as f:
    lines = f.readlines()
    output = lines.pop(0).strip()
    dictionary = {}
    for line in lines:
        if "->" in line:
            pair,middle = line.strip().replace(" ","").split('->')
            dictionary.update({pair:middle})
    print(dictionary)

    for i in range(10):
        check_list = [output[i:i+2] for i in range(0,len(output))]
        for index, combo in enumerate(check_list):
            if dictionary.get(combo):
                check_list[index] = combo[0]+dictionary.get(combo)
                if index == len(check_list):
                    check_list[index] += combo[1]
                output = "".join(check_list)
    print(output)
    c = Counter(output)
    _,most_common = c.most_common()[0]
    _,least_common = c.most_common()[-1]
    print(most_common - least_common)





