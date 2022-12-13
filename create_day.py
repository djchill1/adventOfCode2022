import logging
import os

def create_day_files(day):
    day = str(day)
    try:
        os.mkdir(day)
    except FileExistsError:
        logging.error("Directory ", day, " already exists")
    os.chdir(os.getcwd()+'/'+day)
    # strip leading zeros
    day = str(int(day))
    try:
        open(day+'_input.txt', "x")
    except:
        logging.error("Can't create input file for day " + day + " due to a conflict")
    try:
        open(day + '_test.txt', "x")
    except:
        logging.error("Can't create test file for day " + day + " due to a conflict")
    try:
        f = open(day + '.py', "x")
        f.write('import init\n\ndata = init.read_data(isTest=True, )')
        f.write('\n\n\n\n')
        f.write('\n\n\ndef part1():\n\treturn False')
        f.write('\n\n\ndef part2():\n\treturn False')
        f.write('\n\n\nprint(f\'Part 1: {part1()}, Part 2: {part2()}\')')
        f.close()
    except:
        logging.error("Can't create python file for day " + day + " due to a conflict")

create_day_files('13')