from collections import Counter

def polymer(steps, output):
	for i in range(steps):
		check_list = [output[i:i+2] for i in range(0,len(output))]
		for index, combo in enumerate(check_list):
			if dictionary.get(combo):
				check_list[index] = combo[0]+dictionary.get(combo)
				output = "".join(check_list)
	return output

with open("day14_input") as f:
	lines = f.readlines()
	start = lines.pop(0).strip()
	dictionary = {}
	for line in lines:
		if "->" in line:
			pair,middle = line.strip().replace(" ","").split('->')
			dictionary.update({pair:middle})

	string = polymer(5, start)
	combo_count = dict(Counter([string[i:i+2] for i in range(0,len(string))]))
	letter_count = dict(Counter(string))
	print(combo_count)
	# print(letter_count)
	for _ in range(35):
		tmp_combo = {}

		for combo, num in combo_count.items():
			print(combo, num)
			if dictionary.get(combo):
				add = dictionary.get(combo)
				letter_count.update({add:letter_count.get(add)+num})

				if tmp_combo.get(combo):
					tmp_combo.update({combo:tmp_combo[combo]-num})
				else:
					tmp_combo.update({combo:-num})

				if tmp_combo.get(combo[0]+add):
					tmp_combo.update({combo[0]+add:tmp_combo[combo[0]+add]+num})
				else:
					tmp_combo.update({combo[0]+add:num})
					
				if tmp_combo.get(add+combo[1]):
					tmp_combo.update({add+combo[1]:tmp_combo[add+combo[1]]+num})
				else:
					tmp_combo.update({add+combo[1]:num})


		combo_count = dict(Counter(combo_count) + Counter(tmp_combo))
		print(combo_count)

	c = Counter(letter_count)
	_,most_common = c.most_common()[0]
	_,least_common = c.most_common()[-1]
	print(most_common - least_common)

