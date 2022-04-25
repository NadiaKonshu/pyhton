my_list = list(input('Введите элементы'))
for i in range(1, len(my_list), 2):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list [i]
print(my_list)

# или 2 вариант
# el = 0
# while i < el:
#     my_list.append(input("Введите элементы"))
#     i += 1
# print(my_list)

# или 3 вариант
# my_list = list(input('Введите элементы'))
# for el in range(int(len(my_list) / 2)):
#     my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
#     el += 2
# print(my_list)