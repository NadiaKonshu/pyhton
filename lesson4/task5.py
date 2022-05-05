from functools import reduce

def num_list(n1, n2):
    return n1* n2
my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(num_list, my_list))