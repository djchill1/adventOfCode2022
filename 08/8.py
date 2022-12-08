import init
import numpy as np

data = init.read_data(isTest=True, )

forest_list = []
for row in data:
    row_info = [int(i) for i in row]
    # print(row_info)
    # np.append(forest_matrix, row_info, axis=0)
    forest_list.append(row_info)

forest_matrix = np.array(forest_list)
print(forest_matrix)


# i is the row
# j is the column

def is_visible(matrix, i, j):
    tree_height = matrix[i][j]
    visible = {'left': True, 'right': True, 'above': True, 'below': True}
    trees = {'left': 0, 'right': 0, 'above': 0, 'below': 0}
    print('\nchecking visibility of', tree_height, 'at position', i, j)
    transposition = matrix.transpose()

    # print(transposition[i])
    for iter, value in enumerate(matrix[i]):
        if iter in range(j, 0):
            print('left', value)
            if value >= tree_height:
                visible['left'] = False
                trees['left'] = iter - i
                break
        elif iter == j:
            print('its the value')
            pass
        elif iter in range(j + 1, len(matrix[i])):
            print('right', value)
            if value >= tree_height:
                visible['right'] = False
                trees['right'] = iter - i
                break

    for iter, value in enumerate(transposition[j]):
        if iter in range(i, 0):
            # print('above', value)
            if value >= tree_height:
                visible['above'] = False
                trees['above'] = iter - i
                break
        elif iter == i:
            # print('its the value')
            pass
        elif iter in range(i + 1, len(transposition[j])):
            # print('below', value)
            if value >= tree_height:
                visible['below'] = False
                trees['below'] = iter - i
                break

    print('visible', visible)
    print('trees', trees)
    for value in visible.values():
        if value:
            return True

    return False


def visible_trees(matrix, i, j):
    tree_height = matrix[i][j]
    trees = {'left': 0, 'right': 0, 'above': 0, 'below': 0}
    print('\nchecking visibility of', tree_height, 'at position', i, j)
    transposition = matrix.transpose()


def part1():
    visibile_trees = 0
    for i in range(0, len(forest_matrix)):
        for j in range(0, len(forest_matrix[i])):
            # print(i, j)
            visibility = is_visible(forest_matrix, i, j)
            if visibility:
                visibile_trees += 1
    return visibile_trees


def part2():
    return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
