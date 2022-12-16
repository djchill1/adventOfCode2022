import init

data = init.read_data(isTest=False, )


def manhattan_distance(x0, y0, x1, y1):
	return abs(x0 - x1) + abs(y0 - y1)


points_and_distances = {}
beacons = set()
minx, maxx = 0, 0

for line in data:
	x0, y0, x1, y1 = init.ints(line)
	for value in [x0, x1]:
		if value < minx:
			minx = value
		elif value > maxx:
			maxx = value

	points_and_distances.update({(x0, y0): manhattan_distance(x0, y0, x1, y1)})
	beacons.add((x1, y1))

print('distances', points_and_distances)
print('beacons', beacons)
print(f'min: {minx}, max: {maxx}')


def part1(check_row=10):
	x_cannot_contain_beacons = set()
	for x in range(minx, maxx):
		if (x, check_row) in beacons:
			print(f'index {x}: there is already a beacon at {x}, {check_row}')
			continue
		for sensor_pos, distance in points_and_distances.items():
			# print(sensor_pos, distance)

			if manhattan_distance(x, check_row, sensor_pos[0], sensor_pos[1]) <= distance:
				x_cannot_contain_beacons.add(x)
				# print(f'index {x} cannot host a beacon')
				break
	return len(x_cannot_contain_beacons)


def part2():
	return False

# part 1 answer is not 4411858 (too low)

print(f'Part 1: {part1(2000000)}, Part 2: {part2()}')
