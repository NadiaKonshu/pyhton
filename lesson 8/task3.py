# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
# команду “stop”. При этом скрипт завершается, сформированный список выводится на экран. Подсказка: для данного задания
# примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента необходимо
# реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не
# позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не
# должна завершаться.
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
        # val = int(input('Введите значения и нажмите Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                val = int(input('Введите значения и нажмите Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Недопустимое значение - строка и Bool')
                y_or_n = input(f'Попробовать еще раз? Yes/Stop ')

                if y_or_n == 'Yes' or y_or_n == 'yes':
                    print(try_except.my_input())
                elif y_or_n == 'Stop' or y_or_n == 'stop':
                    return f'Выход'
                else:
                    return f'Выход'


try_except = Error(1)
print(try_except.my_input())
