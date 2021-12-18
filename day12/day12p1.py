
with open("day12_input") as f:
	lines = f.readlines()
	options = {}
	for line in lines:
		node1,node2 = line.strip().split("-")
		if node1 != "end" and node2 != "start":
			if options.get(node1):
				options.get(node1).append(node2)
			else:
				options.update({node1:[node2]})
		if node2 != "end" and node1 != "start":
			if options.get(node2):
				options.get(node2).append(node1)
			else:
				options.update({node2:[node1]})

	print(options)
	print()
	paths = []
	complete_paths = []
	for node in options.pop("start"):
		paths.append(",".join(["start",node]))

	for i in range(30):
		for path in paths[:]:
			node1 = path.split(",")[-1]
			if options.get(node1):
				for node2 in options.get(node1):
					if node2.isupper() or node2 not in path:
						if path+","+node2 not in paths:
							paths.append(path+","+node2)
				paths.remove(path)
			if "end" in path:
				complete_paths.append(path)
				paths.remove(path)

	print(paths)
	print(complete_paths)
	print(len(complete_paths))

		
