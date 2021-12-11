with open("day3_input") as f:
    binaries = f.readlines()
    sums = [0,0,0,0,0,0,0,0,0,0,0,0]
    for binary in binaries:
        for i, bit in enumerate(binary.strip()):
            print(len(binary))
            print(i, bit)
            sums[i]+=int(bit)

    e = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i, bit in enumerate(sums):
        if bit > 500:
            sums[i] = "1"
            e[i]="0"
        else:
            sums[i]="0"
            e[i]="1"
    g="".join(sums)
    e="".join(e)
    print(int(g,2)*int(e,2))
