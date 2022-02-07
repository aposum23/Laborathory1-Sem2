import pandas as pd


def make_table(trains):
    num_lst = []
    end_point_lst = []
    for trn in trains:
        num_lst.append(trn['num'])
        end_point_lst.append(trn['name'])
    data = {'Номер поезда:': num_lst, 'Конечный пункт:': end_point_lst}
    df = pd.DataFrame(data=data)
    print(df)
