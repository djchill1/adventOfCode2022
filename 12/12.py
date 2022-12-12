import init
import numpy as np

data = init.read_data(isTest=False, )

heightmap = np.zeros((len(data), len(data[0])), int)
distance_grid = np.zeros((len(data), len(data[0])), int)

for row, line in enumerate(data):
    for col, value in enumerate(line):
        value = ord(value)
        if value == 83:
            # start, S
            value = 0
        elif value == 69:
            # end, E
            value = 27
        else:
            value -= 96
        heightmap[row, col] = value

print(heightmap)


def find_distance(grid, distance, distance_grid, start_positions, destination_position):
    # recursively find the distance from start to destination positions
    max_row = heightmap.shape[0] - 1
    max_col = heightmap.shape[1] - 1
    starting_locations_to_track = set()

    for row, col in start_positions:
        current_height = grid[row, col]
        distance_grid[row, col] = distance
        for dx, dy in init.adjs:
            nx, ny = row + dx, col + dy

            # ignore if you'd pass the edge of the grid
            if nx == -1 or ny == -1 or nx > max_row or ny > max_col:
                continue

            neighbor = grid[(nx, ny)]

            # if no neighbour, at the boundary so can ignore.
            if neighbor is not None:
                print(
                    f'current position [{row}, {col}] = {current_height} \t checking location [{nx}, {ny}] = {neighbor}')
                target_height = grid[nx, ny]

                # it is possible to move to a location if height is at most one more than current height.
                if target_height <= current_height + 1:

                    # check if a better distance, or can skip.
                    if distance < distance_grid[nx, ny] or distance_grid[nx, ny] == 0:
                        if (nx, ny) == destination_position:
                            # we're there!
                            return distance + 1
                        starting_locations_to_track.add((nx, ny))

    print(starting_locations_to_track)
    if starting_locations_to_track:
        return find_distance(grid, distance + 1, distance_grid, starting_locations_to_track, destination_position)
    return 'Failed'


def part1():
    # find location of start and finish
    start = np.where(heightmap == 0)
    start_pos = set(zip(start[0], start[1]))

    end = np.where(heightmap == 27)
    end_pos = list(zip(end[0], end[1]))[0]

    print(start_pos, end_pos)

    # start at 0, end at 27.
    answer = find_distance(heightmap, 0, distance_grid, start_pos, end_pos)

    return answer


def part2():
    # find location of start and finish
    start = np.where(heightmap == 1)
    start_pos = set(zip(start[0], start[1]))

    end = np.where(heightmap == 27)
    end_pos = list(zip(end[0], end[1]))[0]

    print(start_pos, end_pos)

    # start at 0, end at 27.
    answer = find_distance(heightmap, 0, distance_grid, start_pos, end_pos)

    return answer


print(f'Part 1: {part1()}, Part 2: {part2()}')
