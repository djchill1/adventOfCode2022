import init

data = init.read_data(False, )

global values

def part1():
	length = len(data) - 1
	values = []
	current_sum = 0
	for index, entry in enumerate(data):
		# print(index, entry)
		if entry == '':
			# print('empty', current_sum)
			values.append(current_sum)
			current_sum = 0
		elif index == length:
			current_sum += int(entry)
			values.append(current_sum)
		else:
			current_sum += int(entry)
	print(values)
	return max(values)


def part2():
	length = len(data) - 1
	values = []
	current_sum = 0
	for index, entry in enumerate(data):
		# print(index, entry)
		if entry == '':
			# print('empty', current_sum)
			values.append(current_sum)
			current_sum = 0
		elif index == length:
			current_sum += int(entry)
			values.append(current_sum)
		else:
			current_sum += int(entry)
	print(values)

	value = 0
	for i in range (0,3):
		current_max = max(values)
		values.remove(current_max)
		value += current_max
		print(i, value, current_max)
	return value


print(f'Part 1: {part1()}, Part 2: {part2()}')