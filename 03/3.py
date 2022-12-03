import init
import logging
import re

data = init.read_data(isTest=False, )


def part1():
	score = 0
	for line in data:
		first, second = split_line(line)
		repeated_char = check_repeated_character(first, second)
		# print(repeated_char)
		score += score_character(repeated_char)
	return score


def part2():
	print('## part 2 ##')
	common_vals = []
	score = 0
	length = int(len(data) / 3)
	print('length', length)
	for index in range(0, length):
		index = index * 3
		print('looping', index)
		# print(index, data[index])
		first, second, third = [data[s] for s in range(index, index + 3)]
		print(first, second, third)
		common = check_common_character(first, second, third)
		print('common list', common)
		common = common[0]
		common_vals.append(common)
		print('common', common)
		score += score_character(common)
	print(common_vals)
	return score


def check_repeated_character(a, b):
	for element in a:
		if element in b:
			return element
	logging.error('no repeated character found')


def split_line(line):
	first = line[:len(line) // 2]
	second = line[len(line) // 2:]
	# print(first, second)
	return first, second


def score_character(char):
	value = ord(char)
	if value in range(97, 123):
		# lowercase
		value = value - 96
	else:
		# uppercase
		value = value - 38
	print(char, value)
	return value


def check_common_character(first, second, third):
	commons = []
	for char in first:
		if char in second and char in third:
			commons.append(char)
	return commons


# chars = ['a', 'z', 'A', 'Z']
#
# for char in chars:
# 	value = score_character(char)


print(f'Part 1: {part1()}, Part 2: {part2()}')
