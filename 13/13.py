import init

data = init.read_data(isTest=True, )


def check_ints(l_val, r_val):
    l_val_type, r_val_type = type(l_val), type(r_val)

    if l_val_type == int and r_val_type == int:
        if l_val < r_val:
            return True
        elif r_val > l_val:
            return False
        # otherwise need to check the next value
        else:
            return 'check next'


def part1():
    in_order = []

    for i in range(0, len(data), 3):
        left = eval(data[i])
        right = eval(data[i + 1])
        print(f'\nleft: {left} \t right: {right}')

        for iter, left_value in enumerate(left):
            try:
                right_value = right[iter]
            except:
                print('Right side ran out of items, so inputs are not in the right order')
                in_order.append(0)
                break

            is_correctly_ordered = check_ints(left_value, right_value)
            print(f'Checking {left_value} and {right_value}. Result: {is_correctly_ordered}')
            if is_correctly_ordered == None:
                # wasn't just ints so need to be cleverer


            elif is_correctly_ordered == 'check next':
                continue
            elif is_correctly_ordered:
                in_order.append(1)
                break
            elif not is_correctly_ordered:
                in_order.append(0)
                break

    return in_order


def part2():
    return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
