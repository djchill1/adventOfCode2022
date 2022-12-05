import init
import re

isTest = False

data = init.read_data(isTest=isTest, )

stacks = []
steps = []

is_stacks = True

for line in data:
    # print(line)
    if line == '':
        # print('blank')
        is_stacks = False
        continue
    if is_stacks:
        stacks.append(line)
    else:
        steps.append(line.split(" ")[1:6:2])

# print(stacks)

# for i in range(1, len(stacks[-1]), 4):
#     print(i)

# stacks = [
#     [level[i] for level in stacks if level[i] != ' ']
#     for i in range(1, len(stacks[0]), 4)
# ]

if isTest:
    stacks = ['NZ', 'DCM', 'P']
else:
    stacks = ['PDQRVBHF', 'VWQZDL', 'CPRGQZLH', 'BVJFHDR', 'CLWZ', 'MVGTNPRJ', 'SBMVLRJ', 'JPD', 'VWNCD']

print(stacks, steps)


def part1():
    for step in steps:
        # print(step)
        move_from = int(step[1]) - 1
        move_to = int(step[2]) - 1
        # print(move_from, move_to)
        for i in range(1, int(step[0])+1):
            moving = stacks[move_from][0]
            stacks[move_from] = stacks[move_from][1:]
            # print('moving', i, 'container of value', moving, 'from stack', move_from, 'to stack', move_to)
            stacks[move_to] = moving + stacks[move_to]
            # print('current stacks', stacks)

    final_string = ''
    for entry in stacks:
        final_string = final_string + entry[0]
    return final_string



def part2():
    if isTest:
        stacks = ['NZ', 'DCM', 'P']
    else:
        stacks = ['PDQRVBHF', 'VWQZDL', 'CPRGQZLH', 'BVJFHDR', 'CLWZ', 'MVGTNPRJ', 'SBMVLRJ', 'JPD', 'VWNCD']

    for step in steps:
        print('\n #### starting step', step)
        print('view of stacks before the move', stacks)
        containers_to_move = int(step[0])
        move_from = int(step[1]) - 1
        move_to = int(step[2]) - 1
        print(move_from, move_to)

        moving = stacks[move_from][:containers_to_move]
        stacks[move_from] = stacks[move_from][containers_to_move:]
        print('moving', containers_to_move, 'containers of value', moving, 'from stack', move_from, 'to stack', move_to)
        stacks[move_to] = moving + stacks[move_to]
        print('view of stacks after the move', stacks)

    final_string = ''
    for entry in stacks:
        final_string = final_string + entry[0]
    return final_string


print(f'Part 1: {part1()}, Part 2: {part2()}')
