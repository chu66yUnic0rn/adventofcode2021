def find_next(index, pos, first_i, first_p, last_i, last_p):
	paths = []
	if index < last_i:
		paths.append((index+1, pos))
	if first_i < index:
		paths.append((index-1,pos))
	if pos < last_p:
		paths.append((index,pos+1))
	if first_p < pos:
		paths.append((index, pos-1))
	return paths

def make_map(base_map, current_map_i, current_map_p, size):
	new_map = {}
	add = current_map_i + current_map_p
	for coord, risk in base_map.items():
		i, p = coord
		new_i = i + current_map_i*size
		new_p = p + current_map_p*size
		new_risk = risk + add
		if new_risk > 9:
			new_risk -= 9
		new_map.update({(new_i, new_p):new_risk})
	return new_map

def get_score(base_map, maps, i, p, size):
	current_map_i = i//size
	current_map_p = p//size
	if maps.get((i,p)) is None:
		new_map = make_map(base_map, current_map_i, current_map_p, size)
		maps.update(new_map)
	return maps[(i,p)]

with open("day15_input") as f:
	lines = f.readlines()
	base_map = {}
	maps = {}
	for index, line in enumerate(lines):
		for pos, char in enumerate(line.strip()):
			base_map.update({(index, pos): int(char)})
	
	maps.update(base_map)
	currents = {(0,0):0}
	last_one = []
	# step = 0
	# while (len(lines)*5-1, len(lines[0].strip())*5-1) not in currents.keys():
		# step+= 1
	for step in range(1100):
		steps = {}
		for current, score in currents.items():
			index, pos = current
			# print(index, pos)
			size = len(lines)
			
			results = find_next(index, pos, 0, 0, 5*size-1, 5*size-1)

			for result in results:
				i, p = result
				risk = score + get_score(base_map, maps, i, p, size)

				if steps.get(result) is None or steps.get(result) > risk:
					steps.update({result:risk})
				
		currents = steps
		print(step)
		if currents.get((len(lines)*5-1, len(lines[0].strip())*5-1)):
			last_one.append(currents.get((len(lines)*5-1, len(lines[0].strip())*5-1)))
			print(currents.get((len(lines)*5-1, len(lines[0].strip())*5-1)))
	print(min(last_one))




	

