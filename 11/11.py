import init
import math
import re

data = init.read_data(isTest=False, )


def setup_tests(data):
	tests = []
	starting_worries = []
	operations = []
	for line in data:

		split_line = re.split(' ', line)
		# print(split_line)
		if line == '':
			continue
		elif split_line[0] == 'Monkey':
			monkey = init.ints(line)[0]

		elif split_line[2] == 'Starting':
			starting_worries.append(init.ints(line))
		elif split_line[2] == 'Test:':
			div_by = init.ints(line)[0]
		elif split_line[2] == 'Operation:':
			ignore_me, rule = re.split(' old ', line)
			operations.append(rule)

		elif split_line[5] == 'true:':
			ifTrue = init.ints(line)[0]
		elif split_line[5] == 'false:':
			ifFalse = init.ints(line)[0]
			tests.append([div_by, ifTrue, ifFalse])
	return tests, starting_worries, operations


def new_worry_level(worry, rule, divide_by_three = True):
	# print('\t Monkey inspects an item with a worry level of', worry)

	# find operation to do
	# print(rule)
	op, by_val = re.split(' ', rule)
	if by_val == 'old':
		by_val = worry
	else:
		by_val = int(by_val)
	if rule[0] == '*':
		worry *= by_val
		# print('\t \tWorry level is multiplied by', by_val, 'to', worry)
	else:
		worry += by_val
		# print('\t \tWorry level increases by', by_val, 'to', worry)

	if divide_by_three:
	# after operation, third and round down for handling it
		worry = math.floor(worry / 3)
		print('\t \tMonkey gets bored with item. Worry level is divided by 3 to', worry)

	return worry


def test_monkey(worry, test_rule):
	if worry % test_rule[0] == 0:
		# is divisible
		# print('\t \tCurrent worry level is divisible by', test_rule[0])
		return test_rule[1]
	else:
		# print('\t \tCurrent worry level is not divisible by', test_rule[0])
		return test_rule[2]


def part1(max_rounds = 20):

	inspections = [0, 0, 0, 0, 0, 0, 0, 0]
	round = 1
	monkey_rules, current_worries, operations = setup_tests(data)
	# print(operations)

	while round <= max_rounds:

		for monkey_number, monkey in enumerate(monkey_rules):
			print('Monkey', monkey_number)
			while current_worries[monkey_number]:
				worry = current_worries[monkey_number].pop(0)
				worry = new_worry_level(worry, operations[monkey_number])
				inspections[monkey_number] += 1

				# figure out the monkey to pass this too:
				monkey_to_pass = test_monkey(worry, monkey_rules[monkey_number])
				print('\t \tItem with worry level', worry, 'is thrown to monkey', monkey_to_pass)
				current_worries[monkey_to_pass].append(worry)

		print('\nAfter round', round, ', the monkeys are holding items with these worry levels:')
		for monkey_number, worries in enumerate(current_worries):
			print(monkey_number, ':', inspections[monkey_number], worries)

		round += 1

	return sorted(inspections)[-1] * sorted(inspections)[-2]


def part2(max_rounds = 10000):

	inspections = [0, 0, 0, 0, 0, 0, 0, 0]
	round = 1
	monkey_rules, current_worries, operations = setup_tests(data)
	# print(operations)

	while round <= max_rounds:

		for monkey_number, monkey in enumerate(monkey_rules):
			# print('Monkey', monkey_number)
			while current_worries[monkey_number]:
				worry = current_worries[monkey_number].pop(0)
				worry = new_worry_level(worry, operations[monkey_number], False)
				worry = worry % 936766961130
				inspections[monkey_number] += 1

				# figure out the monkey to pass this too:
				monkey_to_pass = test_monkey(worry, monkey_rules[monkey_number])
				# print('\t \tItem with worry level', worry, 'is thrown to monkey', monkey_to_pass)
				current_worries[monkey_to_pass].append(worry)

		round += 1

	print('\nAfter round', round-1)
	for monkey_number, worries in enumerate(current_worries):
		print(monkey_number, ':', inspections[monkey_number])

	return sorted(inspections)[-1] * sorted(inspections)[-2]



print(f'Part 1: {part1()}, Part 2: {part2()}')
