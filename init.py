import logging
import sys
import typing
import re


def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))


def positive_ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"\d+", s))


adjs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
diags = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
all_dirs = adjs | diags


def manhattan_distance(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def read_data(isTest=False, value='default'):
    current_day = (sys.argv[0].split('/')[-1].split('.')[0])
    if isTest:
        filename = current_day + "_test.txt"
        logging.warning("*** Using Test Data from " + filename)
    else:
        filename = current_day + "_input.txt"
        logging.warning(" Using Data from " + filename)
    with open(filename) as f:
        if value == 'default':
            return f.read().splitlines()
            logging.info("using default parsing")
        elif value == 'int':
            return [int(x) for x in f]
        elif value == 'str':
            return [str(x) for x in f]
        elif value == 'intlist':
            data = f.read()
            return [int(x) for x in data.split(",")]
        else:
            logging.error("Unsupported value of " + value)
