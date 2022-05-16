my_list = [7, 5, 3, 3, 2]
a = int(input('Введите число: '))
for index, number in enumerate(my_list):
    if a <= number:
        continue
    my_list.insert(index, a)
    break
else:
        my_list.append(a)
print(my_list)










