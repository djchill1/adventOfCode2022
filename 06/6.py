import init

data = init.read_data(isTest=False, )




def part1():
	for line in data:
		print(line)
		seen_characters = []
		for iter, value in enumerate(line):
			if value in seen_characters:
				index = seen_characters.index(value)
				print('need to remove to index', index, 'as have seen', value, 'in', seen_characters)
				seen_characters = seen_characters[index+1:]
				print('post removal, have now seen', seen_characters)
			seen_characters.append(value)
			print('now seen', seen_characters)
			if len(seen_characters) == 4:
				print('final characters', seen_characters)
				print('size is', iter+1)
				break
	return iter + 1


def part2():
	for line in data:
		print(line)
		seen_characters = []
		for iter, value in enumerate(line):
			if value in seen_characters:
				index = seen_characters.index(value)
				print('need to remove to index', index, 'as have seen', value, 'in', seen_characters)
				seen_characters = seen_characters[index + 1:]
				print('post removal, have now seen', seen_characters)
			seen_characters.append(value)
			print('now seen', seen_characters)
			if len(seen_characters) == 14:
				print('final characters', seen_characters)
				print('size is', iter + 1)
				break
	return iter + 1


print(f'Part 1: {part1()}, Part 2: {part2()}')