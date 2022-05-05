from math import factorial
from itertools import count


def fibo_gen():
    for el in count(1):
        yield factorial(el)

for step, i in enumerate(fibo_gen(), start=1):
    print('Factorial {} - {}'.format(step, i))
    if step == 5:
        break