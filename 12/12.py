import init
import numpy as np

data = init.read_data(isTest=True, )

heightmap = np.zeros((len(data), len(data[0])), int)

for row, line in enumerate(data):
	for col, value in enumerate(line):
		value = ord(value)
		if value == 83:
			# start, S
			value = 0
		elif value == 69:
			# end, E
			value = 27
		else:
			value -= 96
		heightmap[row, col] = value

print(heightmap)


def part1():

	# Do an A* search to find the right path, maybe this should be it's own function?
	# start at 0, end at 27.
	# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

	# it is possible to move to a location if height is at most one more than current height.
	if target_height > current_height + 1:
		# cannot move to location
		pass

	return False


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')