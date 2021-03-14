import numpy as np


def game_core_v2(r1, r2, number, size):
    t = range(r1, r2)  # создали список с диапазоном нижнего и верхнего порога
    count = 0

    while count < size:
        middle_num = len(t) // 2
        count += 1  # плюсуем попытку
        predict = t[middle_num]
        if number == predict + 1:
            break  # проверка крайних значений на равенство
        elif number == predict - 1:
            break  # проверка крайних значений на равенство
        if number == predict or number == len(t) or number == t[0]:
            break  # выход из цикла,если угадали или угадываемое число равно крайним значениям длины списка
        elif number > predict:
            print(f"Угадываемое число больше {predict} ")
            t = range(predict, predict + middle_num)
        elif number < predict:
            print(f"Угадываемое число меньше {predict} ")
            t = range(predict - middle_num, predict)

    print(f"Вы угадали число {number} за {count} попыток.")
    return count


def score_game(game_core_v2, size):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    r1 = 1 # нижний порог списка
    r2 = 101  # верхний порог списка
    random_array = np.random.randint(r1, r2, size)
    for number in random_array:
        count_ls.append(game_core_v2(r1, r2, number, size))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score
