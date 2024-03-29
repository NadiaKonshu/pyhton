# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class ZeroDivEx(Exception):
    def __init__(self, *args):
        self.data = args

    def __str__(self):
        return ' '.join(map(str, self.args))


if __name__ == '__main__':
    while True:
        ui = input('Введите делитель, для деления 2: ')
        if not ui:
            break
        try:
            num = float(ui)
        except Exception as err:
            print('Введите число!', 'Ошибка')
            continue
        try:
            if num == 0:
                raise ZeroDivEx('На ноль делить нельзя!')
            else:
                print(f'результат деления 5/{num}= {5 / num}')
        except Exception as err:
            print('Ошибка')