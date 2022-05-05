# a
from itertools import count

for el in count(int(input("Введите целое число: "))):
    if el > 10:
        break
    else:
        print(el)
# b

from itertools import cycle

my_list = [2, 4, 6, 7, 4, 9, 1, 0]
iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end='')
    stop = input()
    print(my_list)


