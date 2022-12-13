import init
from collections import deque

data = init.read_data(isTest=True, )


# answer is not: 6456, 6310 (too high)


def create_queue(input_data):
    q = deque()
    # q = init.ints(str(input_data))
    for entry in input_data:
        # if type(entry) is int:
        q.append(entry)

        # elif type(entry) is list:
        #     for value in entry:
        #         q.append(value)
    return q


def de_lister(l_element, r_element, left_q, right_q):
    while type(l_element) is list or type(r_element) is list:
        try:
            if type(l_element) is list:
                to_add = create_queue(l_element)
                while to_add:
                    left_q.appendleft(to_add.pop())
                l_element = left_q.popleft()
        except:
            return 'right', 0, left_q, right_q

        try:
            if type(r_element) is list:
                to_add = create_queue(r_element)
                while to_add:
                    right_q.appendleft(to_add.pop())
                r_element = right_q.popleft()
        except:
            return 'wrong', 0, left_q, right_q
    return l_element, r_element, left_q, right_q


def part1():
    pair_number = 0
    winning_pairs = [0, ]
    for i in range(0, len(data), 3):
        pair_number += 1
        print(f'\n== Pair {pair_number} ==')

        left = eval(data[i])
        right = eval(data[i + 1])
        print(f'- Compare {left} vs {right}')

        left_q = create_queue(left)
        right_q = create_queue(right)

        print(f'  - Queues are {left_q} and {right_q}')

        is_winner = False

        while not is_winner:
            try:
                l_element = left_q.popleft()
            except:
                winning_pairs.append(1)
                print(f'    - Left side ran out of items, so inputs are in the right order')
                break
            try:
                r_element = right_q.popleft()
            except:
                winning_pairs.append(0)
                print(f'    - Right side ran out of items, so inputs are not in the right order')
                break

            l_element, r_element, left_q, right_q = de_lister(l_element, r_element, left_q, right_q)
            # print('dlister', l_element, r_element, left_q, right_q)

            if l_element == 'right':
                winning_pairs.append(1)
                is_winner = True
                print(f'    - Left side ran out of items, so inputs are in the right order')
                break
            elif l_element == 'wrong':
                winning_pairs.append(0)
                is_winner = True
                print(f'    - Right side ran out of items, so inputs are not in the right order')
                break

            print(f'  - Compare {l_element} vs {r_element}')

            while type(l_element) is list and type(r_element) is int:
                r_element = [r_element]

            while type(l_element) is int and type(r_element) is list:
                l_element = [l_element]

            print(f'  - post lists {l_element} vs {r_element}')

            if l_element < r_element:
                winning_pairs.append(1)
                is_winner = True
                print(f'    - Left side is smaller, so inputs are in the right order')
                break

            elif l_element > r_element:
                winning_pairs.append(0)
                is_winner = True
                print(f'    - Right side is smaller, so inputs are not in the right order')
                break

    # sum indexes
    score = 0
    for index, value in enumerate(winning_pairs):
        if value == 1:
            score += index

    return score, winning_pairs


def part2():
    return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
