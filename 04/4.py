import init
import re

data = init.read_data(isTest=False, )


def part1():
	iter = 1
	child_pairs = 0
	for line in data:
		print('running elf pair number', iter)
		first, second = split_line(line)
		print(first, second)
		data_range_first = calculate_range_from_input(first)
		data_range_second = calculate_range_from_input(second)
		print(data_range_first, data_range_second)
		iter += 1

		#is child contained into parent?
		is_subset = fully_contains(data_range_first, data_range_second)
		if is_subset:
			print('second is a subset of the first!')
			child_pairs += 1
		else:
			is_subset = fully_contains(data_range_second, data_range_first)
			if is_subset:
				print('first is a subset of the second!')
				child_pairs += 1

	return child_pairs


def part2():
	print('### Part 2 ###')
	iter = 1
	child_pairs = 0
	for line in data:
		print('running elf pair number', iter)
		first, second = split_line(line)
		print(first, second)
		data_range_first = calculate_range_from_input(first)
		data_range_second = calculate_range_from_input(second)
		print(data_range_first, data_range_second)
		iter += 1

		# is there any overlap?
		has_overlap = has_any_overlap(data_range_first, data_range_second)
		if has_overlap:
			print('there is an overlap!')
			child_pairs += 1

	return child_pairs


def calculate_range_from_input(data):
	data_range = []
	start, end = re.split('-', data)
	for x in range(int(start), int(end) + 1):
		data_range.append(x)
	return data_range


def split_line(line):
	first, second = re.split(',', line)
	return first, second


def fully_contains(parent_list, child_list):
	for entry in child_list:
		if entry not in parent_list:
			return False
	return True


def has_any_overlap(list_1, list_2):
	for entry in list_1:
		if entry in list_2:
			return True
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
