import init
import re

data = init.read_data(isTest=False, )

their_moves = []
my_moves = []

for entry in data:
    their, my = re.split(" ", entry)
    their_moves.append(their)
    my_moves.append(my)


def part1():
    my_score = 0
    for i in range(0, len(their_moves)):
        their = their_moves[i]
        my = my_moves[i]
        print('playing', their, my)
        winner = who_wins(their, my)

        my_score += calculate_scores(my, winner)

    return my_score


def part2():
    # X loose, Y draw, Z win
    my_score = 0
    for i in range(0, len(their_moves)):
        their = their_moves[i]
        outcome = my_moves[i]
        print('playing', their, 'with outcome', outcome)
        my = what_to_pick(their, outcome)
        print('i pick', my)
        winner = who_wins(their, my)

        my_score += calculate_scores(my, winner)

    return my_score


def what_to_pick(their, outcome):
    if outcome == "Y":
        choice = {'A': 'X', 'B': 'Y', 'C': 'Z'}
        return choice[their]
    elif outcome == "Z":
        choice = {'A': 'Y', 'B': 'Z', 'C': 'X'}
        return choice[their]
    else:
        choice = {'A': 'Z', 'B': 'X', 'C': 'Y'}
        return choice[their]


def who_wins(their, my):
    if (their == 'A' and my == 'X') or (their == 'B' and my == 'Y') or (their == 'C' and my == 'Z'):
        return "draw"
    elif (their == 'A' and my == 'Y') or (their == 'B' and my == 'Z') or (their == 'C' and my == 'X'):
        return "my"
    else:
        return "their"


def calculate_scores(my, winner):
    score = 0
    my_scores = {'X': 1, 'Y': 2, 'Z': 3}
    outcome = {'their': 0, 'draw': 3, 'my': 6}
    score += my_scores[my]
    score += outcome[winner]
    print('score', score)
    return score


print(f'Part 1: {part1()}, Part 2: {part2()}')
