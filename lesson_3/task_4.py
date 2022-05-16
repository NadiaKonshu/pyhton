# 1 способ - возведение с помощью **
def my_func(x,y):
    pow = x ** y
    return pow
print(my_func(3,-1))

# 2 способ - возведение с помощью цикла
def my_func(x,y):
    x, y = float(x), int(y)
    ans = x# новая переменная
    for i in range(abs(y) - 1):# -1 тк взяли уже х один раз
        ans = ans * x
    return 1 / ans
print(my_func(3,-1))



