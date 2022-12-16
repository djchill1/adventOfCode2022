import init

data = init.read_data(isTest=False, )


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

	points_and_distances.update({(x0, y0): init.manhattan_distance(x0, y0, x1, y1)})
	beacons.add((x1, y1))

print('distances', points_and_distances)
print('beacons', beacons)
print(f'min: {minx}, max: {maxx}')


def part1(check_row = 10):
	x_cannot_contain_beacons = set()
	beacons_included = 0

	# for each sensor in turn, what indexes can it not allow:
	for beacon in beacons:
		if beacon[1] == check_row:
			x_cannot_contain_beacons.add(beacon[0])
			beacons_included += 1

	for sensor_pos, max_distance in points_and_distances.items():
		remaining_x_distance = max_distance - abs(check_row - sensor_pos[1])
		# print(f'checking {sensor_pos}, with remaining x distance {remaining_x_distance}')
		if remaining_x_distance > 0:
			for x in range(0, remaining_x_distance + 1):
				# print(f'adding indexes {sensor_pos[0] + x} and {sensor_pos[0] - x}')
				x_cannot_contain_beacons.add(sensor_pos[0] + x)
				x_cannot_contain_beacons.add(sensor_pos[0] - x)

	# print(x_cannot_contain_beacons)
	return len(x_cannot_contain_beacons) - beacons_included



def part2():
	return False

# part 1 answer is not 4411858 (too low)

print(f'Part 1: {part1(2000000)}, Part 2: {part2()}')
