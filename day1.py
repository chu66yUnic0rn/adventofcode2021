# def pop_counter(counter):

with open("day1_input") as f:
	depths = f.readlines()
	array_count = len(depths)
	counter = [0,0,0]
	measurements = 0
	previous = 0

	for i, data in enumerate(depths,1):
		print(counter)
		if counter[0]==0:
			counter[0]=int(data.strip())
			continue
		if counter[1]==0:
			counter[0]+=int(data.strip())
			counter[1]=int(data.strip())
			continue
		if counter[2]==0:
			counter[0]+=int(data.strip())
			counter[1]+=int(data.strip())
			counter[2]=int(data.strip())
			current = counter[0]
			counter[0] = counter[1]
			counter[1] = counter[2]
			counter[2] = 0
			if previous != 0:
				if current > previous:
					measurements += 1
			previous = current        
	print(measurements)
