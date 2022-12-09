import init
import re
import numpy as np

data = init.read_data(isTest=False, )


def move_head(pos, direction):
	dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
	return pos[0] + dirs[direction][0], pos[1] + dirs[direction][1]


def move_tail(tail_pos, head_pos):
	diff = (head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1])
	# print('diff', diff)

	x_diff, y_diff = diff

	if x_diff == 2 and y_diff == 2:
		target_diff = (-1, -1)
	elif x_diff == -2 and y_diff == -2:
		target_diff = (1, 1)
	elif x_diff == -2 and y_diff == 2:
		target_diff = (1, -1)
	elif x_diff == 2 and y_diff == -2:
		target_diff = (-1, 1)
	elif x_diff == 2:
		target_diff = (-1, 0)
	elif x_diff == -2:
		target_diff = (1, 0)
	elif y_diff == 2:
		target_diff = (0, -1)
	elif y_diff == -2:
		target_diff = (0, 1)
	else:
		return tail_pos

	return head_pos[0] + target_diff[0], head_pos[1] + target_diff[1]


def part1():
	head_pos, tail_pos = [(0, 0), (0, 0)]
	tail_visited = [(0, 0)]

	for entry in data:
		direction, distance = re.split(' ', entry)
		distance = int(distance)
		# print(direction, distance)

		for i in range(0, distance):

			# move head
			head_pos = move_head(head_pos, direction)

			# move tail
			tail_pos = move_tail(tail_pos, head_pos)
			# print('New positions. head:', head_pos, 'tail:', tail_pos)

			if tail_pos not in tail_visited:
				tail_visited.append(tail_pos)

	return len(tail_visited)


def part2():
	print('#### PART 2')
	positions = [(0,0) for i in range(0,10)]
	tail_visited = [(0, 0)]

	for entry in data:
		direction, distance = re.split(' ', entry)
		distance = int(distance)
		print('\n', direction, distance)

		for i in range(0, distance):
			print()

			# move head
			positions[0] = move_head(positions[0], direction)

			# move tails
			for j in range(1, 10):
				# print('moving knot #', j)
				positions[j] = move_tail(positions[j], positions[j-1])
				print('New positions:', positions)

			if positions[9] not in tail_visited:
				tail_visited.append(positions[9])

	# print(tail_visited)
	return len(tail_visited)


print(f'Part 1: {part1()}, Part 2: {part2()}')
