#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from package import *


if __name__ == '__main__':
    flag = True
    trains = []
    while flag:
        print('\n')
        MakeTable.make_table(trains)
        print('\n')
        print('1. Добавить новый поезд')
        print('2. Вывести информацию о поезде')
        print('3.Выход из программы')
        com = int(input('введите номер команды: '))
        if com == 1:
            trains.append(AddElement.add_element())
        elif com == 2:
            train_num = input('Введите номер поезда: ')
            FindTrain.find_train(trains, train_num)
        elif com == 3:
            flag = False
