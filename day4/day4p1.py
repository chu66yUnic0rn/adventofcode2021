from collections import Counter

class Board:
    def __init__(self):
        self.numbers = []
        self.hits = []

    def add_numbers(self, numbers):
        self.numbers.append(numbers)

    def find_hits(self, draw):
        tmp_vertical = []
        for number_line in numbers:
            for index, num in enumerate(number_line.split(" ")):
                if draw == num:
                    self.hits.append(number_line)
                    for i in range(5):
                        tmp_vertical.append(self.numbers[i].split(" ")[index])
                    self.hits.append(" ".join(tmp_vertical))
        top_hit = Counter(self.hits).most_common(1)
        if top_hit[0][1] == 5:
            return top_hit[0][0]
        return None

with open("day4_input") as f:
    lines = f.readlines()
    draws = lines[0].strip().split(',')
    lines.pop(0)
    lines.pop(0)
    lines.append("\n")
    boards = []
    for i in range(0, len(lines), 6):
        new_board = Board()
        new_board.add_numbers(lines[i])





