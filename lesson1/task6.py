a = int(input("Результат в километрах в первый день пробежки"))
b = int(input("Общий результат спортсмена в километрах"))
day = 1
while a < b:
    print(f"{day}-й день: {a:.2f}")
    a += a * 0.1
    day = day + 1
print(f"На {day}-й день спортсмен достиг результата - не менее {b}км")