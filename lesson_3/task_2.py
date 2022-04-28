def my_f(**kwargs):
    return kwargs

print(my_f(
        name=input('name:') ,
        surname=input('surname:'),
        year=input('Год рождения:'),
        city=input('Город:'),
        email=input('Эл. почта:'),
        tel=input('Телефон:'),
))
