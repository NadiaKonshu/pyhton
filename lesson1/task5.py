revenue = float(input('Введите значение выручки:'))
cost = float(input('Введите значение издержек:'))
profit = revenue - cost
if profit > 0:
    rentable_revenue = profit / revenue
    print(f'Прибыль: {profit:.2f} Рентабельность: {rentable_revenue:.2f}')
    employees = int(input('Введите количество сотрудников фирмы:'))
    profit_employees = profit / employees
    print(f'Прибыль фирмы на сотрудника: {profit_employees:.2f}')
elif profit < 0:
    print('Убыток')
else:
    print('Работа в ноль')