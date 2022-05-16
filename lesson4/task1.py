import sys

hours, salary, bonus = map(float, sys.argv[1:])
print('salary - {}'.format(hours * salary + bonus))