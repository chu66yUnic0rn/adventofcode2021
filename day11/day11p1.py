
def steps(num, octopus):
	added = []
	total_flash = 0
	for i in range(num):
		for coord, char in octopus.items():
			octopus[coord]=char+1
			added.append(coord)
		total_flash += try_flash(added, octopus)
	return octopus, total_flash


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
	print(steps(100,octopus))
			

