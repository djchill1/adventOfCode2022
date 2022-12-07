import init

data = init.read_data(isTest=False, )


filesystem = {'/': {}}
ref = filesystem

sizes = []

i = 0

while i < len(data):
    command = data[i].split()
    print(command)

    if command[1] == "cd":
        if command[2] != '..':
            ref[command[2]][".."] = ref

        ref = ref[command[2]]
    elif command[1] != "ls":
        if command[0] == 'dir':
            ref[command[1]] = {}
        else:
            ref[command[1]] = int(command[0])

    i += 1
    # print(ref)

# print(ref)


def get_sizes(files):
    global sizes
    size = 0

    for name in files:
        if name == "..":
            continue

        if type(files[name]) is dict:
            size += get_sizes(files[name])
        else:
            size += files[name]

    sizes.append(size)
    return size


get_sizes(filesystem["/"])


def part1():
    score = 0
    for item in sorted(sizes):
        if item <= 100000:
            score += item
    return score


def part2():
    size = next(size for size in sorted(sizes) if size >= sizes[-1] - 40000000)
    return size


print(f'Part 1: {part1()}, Part 2: {part2()}')
