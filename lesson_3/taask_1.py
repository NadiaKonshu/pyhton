def my_f(arg_1, arg_2):
    try:
        quo = arg_1 / arg_2
        return quo
    except ZeroDivisionError:
        return print('На ноль делить нельзя!')
arg_1 = int(input('Введите делимое'))
arg_2 = int(input('Введите делитель'))
print(my_f(arg_1, arg_2))

