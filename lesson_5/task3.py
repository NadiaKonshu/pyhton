with open('salaries.txt', encoding='utf-8') as f:
    lines = f.readlines()

salaries = []
for line in lines:
    name, salary = line.split()
    salaries.append(float(salary))
    if float(salary) < 20000.00:
        print(line, end='')
print('\nСредний доход:', sum(salaries) / len(salaries))
