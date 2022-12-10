import init
import re
import numpy as np

data = init.read_data(isTest=False, )


def cycle(data):
	x_vals = [1]
	x_vals_during_cycle = [1]
	for line in data:

		if line[0:4] == 'noop':
			# one cycle
			x_vals.append(x_vals[-1])
			x_vals_during_cycle.append(x_vals[-1])
			pass
		else:
			# addx
			# 2 cycles
			x_vals.append(x_vals[-1])
			x_vals.append(x_vals[-1])

			x_vals_during_cycle.append(x_vals[-1])
			x_vals_during_cycle.append(x_vals[-1])

			command, size = re.split(' ', line)

			# after the cycle
			x_vals[-1] = x_vals[-1] + int(size)

	print(line, 'during vals:', x_vals_during_cycle)
	print(line, 'ending vals:', x_vals)
	return x_vals, x_vals_during_cycle


def part1():
	x_vals, x_vals_during_cycle = cycle(data)

	# calculate signal strengths
	print(len(x_vals_during_cycle))
	vals_to_score = [20, 60, 100, 140, 180, 220]
	total_score = 0
	for value in vals_to_score:
		if value < len(x_vals_during_cycle):
			inter_score = value * x_vals_during_cycle[value]
			total_score += inter_score
			print('score', value, x_vals_during_cycle[value], 'total', inter_score)
	return total_score


def part2():
	print('\n ##### part 2')
	x_vals, x_vals_during_cycle = cycle(data)

	visibles = []
	printer = []
	sprite_pos = [0, 1, 2]
	cycle_number = 0

	for iter, entry in enumerate(x_vals_during_cycle):
		cycle_number += 1
		if iter == 0:
			cycle_number -= 1
			continue
		position = (cycle_number - 1) % 40
		if position in sprite_pos:
			visibles.append('#')
		else:
			visibles.append('.')
		print('start cycle', cycle_number)
		print('during cycle', cycle_number, ': draw pixel in position', position)
		# print('current val \t', entry)
		print('current CRT \t', visibles)

		if entry != x_vals[iter]:
			# change the sprite_pos
			new_middle = x_vals[iter]
			sprite_pos = [new_middle - 1, new_middle, new_middle + 1]
			# print(entry, x_vals[iter])
			print('sprite position:', sprite_pos)
			print('\n')

		if iter % 40 == 0 and iter != 0:
			printer.append(visibles)
			# new row
			visibles = []



	print('\n part 2 result is the letters below:')
	for line in printer:
		print(line)
	print('\n')

	return 'CHECK WHAT IS PRINTED IN CONSOLE!'


print(f'Part 1: {part1()}, Part 2: {part2()}')