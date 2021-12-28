from collections import Counter

class Board:
	def __init__(self):
		self.numbers = {}
		self.hits = []

	def add_numbers(self, row, numbers):
		self.numbers.update({row:numbers})

	def find_hits(self, draw):
		for row, nums in self.numbers.items():
			if draw in nums:
				index = nums.index(draw)
				if (row, index) not in self.hits:
					self.hits.append((row,index))
					row_hit = Counter(hit[0] for hit in self.hits)
					index_hit = Counter(hit[1] for hit in self.hits)
					if row_hit.most_common(1)[0][1] == 5 or index_hit.most_common(1)[0][1] == 5:
						return self
		return None

	def calculate_score(self, last_called):
		unmarked = 0
		for row, nums in self.numbers.items():
			for i in range(len(nums)):
				if (row,i) not in self.hits:
					unmarked += int(nums[i])
		print(unmarked)
		return unmarked*int(last_called)

with open("day4_input") as f:
	lines = f.readlines()
	draws = lines[0].strip().split(',')
	lines.pop(0)
	lines.pop(0)
	lines.append("\n")
	boards = []
	for i in range(0, len(lines), 6):
		new_board = Board()
		for x in range(5):
			new_board.add_numbers(x,lines[i+x].split())
		boards.append(new_board)
		print(new_board.numbers.items())
	# print(boards)
	for draw in draws:
		print(draw)
		for board in boards:
			result = board.find_hits(draw)
			if result is not None:
				print(result.numbers)
				print(result.calculate_score(draw))
				break
		else:
			continue
		break







