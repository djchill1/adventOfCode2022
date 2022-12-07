import init
import re

data = init.read_data(isTest=False, )

# dict structure:
# {'high level directory': [total size, child dir 1, child dir 2], etc.}
structure = {'/': [0]}


def create_structure(data):
    current_dir = '/'
    prev_dirs = []
    folders = []
    for iter, line in enumerate(data):
        if line[:4] == '$ cd':
            # print('reading line', line)
            # change directory
            a, move_to_dir = re.split(' cd ', line)
            if move_to_dir == '..':
                # move up a level
                move_to_dir = prev_dirs.pop(-1)
            elif move_to_dir == '/':
                prev_dirs = []
            else:
                prev_dirs.append(current_dir)
                if move_to_dir not in folders:
                    folders.append(move_to_dir)
            current_dir = move_to_dir
            # print('## directory now', current_dir)

        elif line[:4] == '$ ls':
            # list contents and add to dict until next $
            # print('reading line', line)
            # print('## adding to dict for', iter)
            info = get_list_of_files(iter, data)
            # print(info)
            structure.update({current_dir: info})

    print(structure)

    final_scores = {}

    print('fixing structure')
    print(folders)

    while folders != []:
        for folder in folders:
            score, nested_folders = structure[folder]
            print(folder, nested_folders, score)
            if nested_folders == []:
                final_scores.update({folder: score})
                folders.remove(folder)
            for sub_folder in nested_folders:
                if sub_folder in final_scores:
                    # add the score to the main folder
                    score += final_scores[sub_folder]
                    final_scores.update({folder: score})

                    # remove subfolder from list.
                    nested_folders.remove(sub_folder)
                    structure.update({folder: [score, nested_folders]})
                    pass
                else:
                    pass

    # work back through structure to add up sums of whats contained within each folder.

    # create a final structure, remember indirectly held items count too!
    # for key, value in structure.items():
    #     print('working through', key, value)
    #     size = value[0]
    #     for folder in value[1]:
    #         print('folder', folder)
    #         print(structure[folder])
    #         size += structure[folder][0]
    #         print(structure[folder][0])
    #         print(key, value, folder, size)

    return final_scores


def get_list_of_files(iter, data):
    dirs = []
    size = 0
    still_list = True
    iter += 1
    while still_list and iter < len(data):
        # print(data)
        info = re.split(' ', data[iter])
        size_or_dir_or_command = info[0]
        dir_name_or_file_name = info[1]
        if size_or_dir_or_command == '$':
            still_list = False
            break
        elif size_or_dir_or_command == 'dir':
            dirs.append(dir_name_or_file_name)
        else:
            size += int(size_or_dir_or_command)
        # print('reading line', data[iter])
        iter += 1

    return [size, dirs]


def calculate_score(final_scores, max_folder_size):
    score = 0
    for key, value in final_scores.items():
        if value <= max_folder_size:
            print('score value being taken into account', key, value)
            score += value
    return score


def part1():
    final_scores = create_structure(data)
    print(final_scores)
    return calculate_score(final_scores, 100000)


def part2():
    return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
