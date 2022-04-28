def summary():
    ex = False
    result = 0
    while ex == False:
        numbers = input('введите числа или q для завершения').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line += int(num)
        result += res_line
        print(result)
    return result
summary()