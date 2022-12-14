import init
import re

data = init.read_data(isTest=False, )


def part1():
    blocked_points = set()

    biggest_y = 0
    for line in data:
        pairs = re.split(' -> ', line)
        print(pairs)

        for i in range(len(pairs) - 1):
            a, b = pairs[i], pairs[i + 1]
            a, b = init.ints(a), init.ints(b)
            biggest_y = max(biggest_y, int(a[1]))
            biggest_y = max(biggest_y, int(b[1]))
            print(a, b)

            for xx in range(min(int(a[0]), int(b[0])), max(int(b[0]) + 1, int(a[0]) + 1)):
                for yy in range(min(int(a[1]), int(b[1])), max(int(b[1]) + 1, int(a[1]) + 1)):
                    blocked_points.add((xx, yy))

    print(blocked_points)

    sand_placed = 0

    while True:
        sand_x, sand_y = 500, 0
        iter_count = 0

        # loop to find where the sand grain ends up
        while True:
            iter_count += 1
            if iter_count > 700:
                # likely fell off the edge
                return sand_placed

            if (sand_x, sand_y + 1) not in blocked_points:
                # can continue straight down as not blocked
                sand_y += 1
                continue
            else:
                if (sand_x - 1, sand_y + 1) not in blocked_points:
                    # diagnoally down left as not blocked
                    sand_x -= 1
                    sand_y += 1
                    continue
                elif (sand_x + 1, sand_y + 1) not in blocked_points:
                    # diagnoally down right as not blocked
                    sand_x += 1
                    sand_y += 1
                    continue

            # if here, then the sand stops in current location
            blocked_points.add((sand_x, sand_y))
            sand_placed += 1
            break


def part2():
    blocked_points = set()

    biggest_y = 0
    for line in data:
        pairs = re.split(' -> ', line)
        print(pairs)

        for i in range(len(pairs) - 1):
            a, b = pairs[i], pairs[i + 1]
            a, b = init.ints(a), init.ints(b)
            biggest_y = max(biggest_y, int(a[1]))
            biggest_y = max(biggest_y, int(b[1]))
            print(a, b)

            for xx in range(min(int(a[0]), int(b[0])), max(int(b[0]) + 1, int(a[0]) + 1)):
                for yy in range(min(int(a[1]), int(b[1])), max(int(b[1]) + 1, int(a[1]) + 1)):
                    blocked_points.add((xx, yy))

    print(blocked_points)

    # only adding 1 as that's the lowest we want the sand to be. (floor would be 1 level lower)
    lowest_possible_y = biggest_y + 1
    print('lowest sand at', lowest_possible_y)

    sand_placed = 0

    while True:
        sand_x, sand_y = 500, 0

        # complete if the start position already blocked
        if (sand_x, sand_y) in blocked_points:
            return sand_placed

        # loop to find where the sand grain ends up
        while True:
            if sand_y == lowest_possible_y:
                # at the floor
                blocked_points.add((sand_x, sand_y))
                sand_placed += 1
                print(f'Placed sand at {sand_x}, {sand_y}. Current count {sand_placed}')
                break

            if (sand_x, sand_y + 1) not in blocked_points:
                # can continue straight down as not blocked
                sand_y += 1
                continue
            else:
                if (sand_x - 1, sand_y + 1) not in blocked_points:
                    # diagnoally down left as not blocked
                    sand_x -= 1
                    sand_y += 1
                    continue
                elif (sand_x + 1, sand_y + 1) not in blocked_points:
                    # diagnoally down right as not blocked
                    sand_x += 1
                    sand_y += 1
                    continue

            # if here, then the sand stops in current location
            blocked_points.add((sand_x, sand_y))
            sand_placed += 1
            print(f'Placed sand at {sand_x}, {sand_y}. Current count {sand_placed}')
            break


print(f'Part 1: {part1()}, Part 2: {part2()}')
