from datetime import datetime


def add_element():
    name = input('Конечный пункт: ')
    num = input('Номер поезда: ')
    tm = datetime.strptime(input('Время отправления: '), '%Y-%m-%d %H:%M')
    trains = {}
    trains['name'] = name
    trains['num'] = int(num)
    trains['tm'] = tm
    return trains
