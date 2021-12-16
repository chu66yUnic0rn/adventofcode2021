
def steps(num, octopus):
	added = []
	first_all = 0
	for i in range(num):
		for coord, char in octopus.items():
			octopus[coord]=char+1
			added.append(coord)
		num_flashes = try_flash(added, octopus)
		if num_flashes == len(octopus):
			return octopus, i+1
	return octopus, None


def try_flash(added, octopus):
	flashed = []
	while len(added)!=0:
		# print(added)
		for index, pos in added[:]:
			added.remove((index,pos))
			if octopus[(index,pos)] > 9:
				octopus[(index,pos)]=0
				flashed.append((index,pos))
				print("flashing", index,pos)
				i,p = list(octopus)[-1]
				if index > 0:
					octopus[(index-1,pos)]+=1
					added.append((index-1,pos))
				if pos > 0:
					octopus[(index,pos-1)]+=1
					added.append((index,pos-1))
				if index < int(i):
					octopus[(index+1,pos)]+=1
					added.append((index+1,pos))
				if pos < int(p):
					octopus[(index,pos+1)]+=1
					added.append((index,pos+1))
				if index > 0 and pos > 0:
					octopus[(index-1,pos-1)]+=1
					added.append((index-1,pos-1))
				if index > 0 and pos < int(p):
					octopus[(index-1,pos+1)]+=1
					added.append((index-1,pos+1))
				if index < int(i) and pos > 0:
					octopus[(index+1,pos-1)]+=1
					added.append((index+1,pos-1))
				if index < int(i) and pos < int(p):
					octopus[(index+1,pos+1)]+=1
					added.append((index+1,pos+1))
	for point in flashed:
		octopus[point] = 0
	return len(flashed)

with open("day11_input") as f:
	lines = f.readlines()
	octopus = {}
	for index,line in enumerate(lines):
		for pos, char in enumerate(line.strip()):
			octopus.update({(index, pos): int(char)})
	
	#print(octopus)
	print(steps(1000,octopus))
			

