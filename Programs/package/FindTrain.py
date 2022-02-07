def find_train(trains, num):
    for dcts in trains:
        if dcts['num'] == num:
            print(f'Конечный пункт: {dcts["name"]} \n'
                  f'Номер поезда: {dcts["num"]} \n'
                  f'Время отправления: {(dcts["tm"])}')
            return
    print('Поезда с таким номером нет')
