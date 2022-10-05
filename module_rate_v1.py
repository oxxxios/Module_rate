while True:
    level_one_kol = int(input('Введите количествооценок за первый уровень - '))
    if level_one_kol == 1:
        level_one_num = int(input('Введите оценку за первый уровень - '))
        if level_one_num > 5:
            print('Такой оценки нет ')
            continue
        else:
            level_one = level_one_num * 0.6

            level_two_kol = int(input('Введите количество оценок за второй уровень - '))
            if level_two_kol == 1:
                level_two_num = int(input('Введите оценку за второй уровень - '))
                if level_two_num > 5:
                    print('Такой оценки нет ')
                    continue
                else:
                    level_two = level_two_num * 0.8

                    level_three_kol = int(input('Введите количество оценок за третий уровень - '))
                    if level_three_kol == 1:
                        level_three_num = int(input('Введите оценку за третий уровень - '))
                        if level_three_num > 5:
                            print('Такой оценки нет ')
                            continue
                        else:
                            level_three = level_one_num * 1

                            bal_kol= int(input('Введите количество оценок  вашего жб - '))
                            bal_num = int(input('Введите ваш журнальный бал - '))
                            if bal_kol == 1 and bal_num < 5:
                                bal = bal_num * 0.6
                                number = (level_one + level_two + level_two) / 3
                                print(number)
                            else:
                                print('что то не так')

























