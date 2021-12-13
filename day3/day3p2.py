with open("day3_input") as f:
    binaries = f.readlines()
    current_ox = binaries
    current_co2 = binaries
    for i in range(12):
        print(len(current_ox))
        team1 = []
        team0 = []
        for binary in current_ox[:]:
            if binary.strip()[i] == "1":
                team1.append(binary.strip())
            else:
                team0.append(binary.strip())
        if len(team1) >= len(team0):
            current_ox=team1
            print("team 1 selected" + str(len(team1)))
            
        else:
            current_ox=team0
            print("team 0 selected" + str(len(team0)))

    for i in range(12):
        print(len(current_co2))
        team1 = []
        team0 = []
        for binary in current_co2[:]:
            if binary.strip()[i] == "1":
                team1.append(binary.strip())
            else:
                team0.append(binary.strip())
        if len(team1)*len(team0) == 0:
            break
        if len(team1) < len(team0):
            current_co2=team1
            print("team 1 selected" + str(len(team1)))
            
        else:
            current_co2=team0
            print("team 0 selected" + str(len(team0)))


    oxygen = current_ox[0]
    co2 = current_co2[0]
    print(int(oxygen,2)*int(co2,2))

