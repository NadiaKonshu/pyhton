with open('programfile.txt', 'w') as f:
    while True:
        line = input('Введите строку: ')
        if line == ' ':
            break
        f.write(line + '\n')