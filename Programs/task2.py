#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import module


if __name__ == '__main__':
    flag = True
    trains = []
    while flag:
        print('\n')
        module.make_table(trains)
        print('\n')
        print('1. Добавить новый поезд')
        print('2. Вывести информацию о поезде')
        print('3.Выход из программы')
        com = int(input('введите номер команды: '))
        if com == 1:
            trains.append(module.add_element())
        elif com == 2:
            train_num = input('Введите номер поезда: ')
            module.find_train(trains, train_num)
        elif com == 3:
            flag = False
