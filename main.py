import sys
import os
import importlib

CURRENT_DAY=15
# sys.path.append('1')
# day1 = __import__('day1')

import utils
import shutil

def readFile(day, type):
    if type == 's':
        f = open(day + '/sample.txt', 'r')
    if type == 'i':
        f = open(day + '/input.txt', 'r')
    return f


def run(day, type, part):
    sys.path.append(day)
    mod = importlib.import_module('day'+day)
    f = readFile(day, type)
    
    # day1.solv1(f)
    # print(globals())
    # m = globals()['day1']
    func = getattr(mod, 'solv' + str(part))
    func(f)

def create(day):
    path = day
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    print(isExist)
    if not isExist:
      # Create a new directory because it does not exist 
        os.makedirs(path)
        f = open(path + '/sample.txt', 'x')
        f.close()
        f = open(path + '/input.txt', 'x')
        f.close()
        # f = open(path + '/day'+day+'.py', 'x')
        # f.close()
        shutil.copyfile('example.py', path + '/day'+day+'.py')
        print("Day" + day + " is created!")


# for i in range(1, CURRENT_DAY+1):
#     print('*'*30)
#     print('Day ', i, ':')
#     for j in range(1, 3):
#         print('\tPart ', j)
#         print('\t\tsample', '-'*2)
#         run(str(i), 's', j)
#         print('\t\tinput', '-'*2)
#         run(str(i), 'i', j)

# create(str(CURRENT_DAY))
# run(str(CURRENT_DAY), 's', 1)
# run(str(CURRENT_DAY), 'i', 1)
# run(str(CURRENT_DAY), 's', 2)
run(str(CURRENT_DAY), 'i', 2)
