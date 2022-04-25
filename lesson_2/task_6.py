units = []
features = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
num = 0
while True:
    if input('выход - Q,\nДругая клавиша - продолжить: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input(f'{f}: ')
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
        units.append((num, features.copy()))
        print("Аналитика по товарам:\n")
        for key, value in analitics.items():
            print(key, value)




