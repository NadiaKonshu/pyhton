n = int(input('Введите целое положительное число'))
max = 0
num = n
while num > 0:
    end_num = n % 10
    if end_num > max:
        max = end_num
    if max == 9:
        break
    num = num // 10
print(f'Самая большая цифра в числе {n}:', max)