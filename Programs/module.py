from datetime import datetime
import pandas as pd


def add_element():
    name = input('Конечный пункт: ')
    num = input('Номер поезда: ')
    tm = datetime.strptime(input('Время отправления: '), '%Y-%m-%d %H:%M')
    trains = {}
    trains['name'] = name
    trains['num'] = int(num)
    trains['tm'] = tm
    return trains


def find_train(trains, num):
    for dcts in trains:
        if dcts['num'] == num:
            print(f'Конечный пункт: {dcts["name"]} \n'
                  f'Номер поезда: {dcts["num"]} \n'
                  f'Время отправления: {(dcts["tm"])}')
            return
    print('Поезда с таким номером нет')


def make_table(trains):
    num_lst = []
    end_point_lst = []
    for trn in trains:
        num_lst.append(trn['num'])
        end_point_lst.append(trn['name'])
    data = {'Номер поезда:': num_lst, 'Конечный пункт:': end_point_lst}
    df = pd.DataFrame(data=data)
    print(df)
