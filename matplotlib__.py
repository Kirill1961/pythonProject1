import math

import matplotlib.pyplot as plt
from collections import Counter
from math import sqrt
# years = [1982, 1984, 1990, 1999, 2004, 2005, 2009, 2012, 2017, 2020]
# gdp = [110.2, 375, 762, 1245, 1425, 852, 9320, 18530, 45700, 64102]
# plt.plot(years, gdp, color='green')
# plt.title('Моя ЗП')
# plt.xlabel('годики')
# plt.ylabel('рублики')
# plt.show()


# years = [20, 100, 250, 400, 670, 940]
# vvp = [5, 15, 40, 84, 124, 187]
# plt.plot(years, vvp)
# plt.title('PROBE')
# plt.ylabel('this Y')
# plt.xlabel('this X')
# plt.show()


# movies = ['Entony', 'Ben', 'Kasablanka', 'Handy', 'West']
# num_oscars = [5, 11, 3, 8, 10]

# xs = [i + 0.1 for i, _ in enumerate(movies)]
# plt.bar(xs, num_oscars)
# plt.xticks([i + 0.5 for i,_ in enumerate(movies)], movies)
# plt.ylabel('MEDAL')
# plt.xlabel('FILMS')
# plt.show()

# grades = [91, 15, 20, 74, 30, 40, 0, 58, 63, 87, 112]
# decil = lambda grade: grade // 10 * 10  # деление без остатка и оставили десятую часть числа
# histogramm = Counter(decil(grade) for grade in grades)
# print(histogramm)


# num_friends = [3]
num_friends = [100, 92, 87, 74, 56, 37, 21, 12, 2]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]  # friend_counts это словарь из Counter, если ключ [x]
# не соотв ключам из словаря то ys - равен 0
# print(xs)
print(friend_counts, '  friend_counts')
print(ys, ' ys')
plt.bar(xs, ys)

plt.axis([0, 101, 0, 20])  # пределы оси Х и У,  / axis([xmin, xmax, ymin, ymax]) /
# plt.show()

lagerst_value = max(num_friends)
smallest_value = min(num_friends)
print(lagerst_value, smallest_value)

num_friends_three = [100, 49, 41, 40, 25]
# определим центр данных для num_friends

def mean(x):
    return sum(x) / len(x)


print(mean(num_friends_three), ' среднее варриационного ряда')


# КВАНТИЛЬ - значение меньше которого расположен определённый процент данных (наблюдений)
# , МЕДИАНА - это значение меньше которого расположены 50% данных (наблюдений)

def quantile(x, p):
    p_index = int(p * len(x))  # преобразовали квантиль " р " в индеккс списка " х "
    print(p_index)
    return sorted(x)[p_index]  # возвр. значение из списка " х " соответсвующее заданному квантилю


print(quantile(num_friends, 0.25), '  0.25 КВАНТИЛЬ  значение меньше которого расположен определённый процент данных')
print(quantile(num_friends, 0.75), ' квантиль уровня 0.75')

# Используем МОДУ, которая определяет значение встречающееся наиболее часто

num_friends_two = [ 100, 92, 87, 74, 74, 56, 37, 21, 12, 12,  2]


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    print(max_count, ' max_count')
    return [(x_i, count) for x_i, count in counts.items() if count == max_count]


print(mode(num_friends_two), ' mode, модальный интервал - определяет значение встречающееся наиболее часто')



# ВАРИАЦИИ - отражают меру изменчивости данных, ближе к 0 ВАР., меньше,у больших знач - больше.
# " Размах " один из показателей :

def data_range(x):
    return max(x) - min(x)
print(data_range(num_friends_two), ' Размах один из показателей вариации')
print('  ')


# ДИСПЕРСИЯ - средняя сумма квадратов откллоенений от среднего
num_friends_three = [3450, 3550, 3650, 3420, 3680, 3550]
# data_for_covar = [39, 41, 43, 45, 47]
# num_friends_three = [100, 49, 41, 40, 25]
# num_friends_three = [10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80]
print('num_friends_three    ', num_friends_three)
print('  ')
def de_mean(x):
    x_bar = mean(x) # Среднее арифметическое коллекции
    print(x_bar, '   x_bar среднее арифметическое варриационного ряда')
    print('  ')
    return [x_i - x_bar for x_i in x] # среднее результата будет равно нулю
print(de_mean(num_friends_three ), '         отклонение от среднего = варианта минус среднее ')



def variance(x):  # ДИСПЕРСИЯ Или variance
    n = len(x)
    deviations = de_mean(x)
    print(n, ' длинна списка', deviations, ' deviations')
    sum_of_squares = [y**2 for y in deviations] # прокручиваем отклонения и возводим в квадрат
    print('  ')
    print(sum_of_squares, ' квадрат отклонения от среднего')
    print('  ')
    print(sum(sum_of_squares), '       сумма квадратов')
    print('  ')
    variance_su_sq = (sum(sum_of_squares))/(n - 1)
    print (variance_su_sq,'   ДИСПЕРСИЯ (variance) - это сумма квадратов отклонения / (n - 1) для', num_friends_three )
    # print('  ')
    # std = math.sqrt(variance_su_sq)
    # print(std, '    std вычисление в теле ф-ции')
    print('  ')
    return sum(sum_of_squares)/(n-1)  # возврат вычисленного значения в точку вызова standart_deviations(х)
# print(variance(num_friends_three ))



""" std - standart_deviations квадратный корень из дисперсии"""

def standart_deviations(x):
    return math.sqrt((variance(x))) # вызов ф-ции variance(x)
print(standart_deviations(num_friends_three ), '  std, среднеквадратичное отклонение - знач дисперсии из variance(x)')

print('////////////////////////////////////  ')

# Интерквантильный размах

def interquantil_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)
print(interquantil_range(num_friends_three), ' Интерквантильный размах')


print('  ')

# Коэффициент вариации (CVar) определяется как отношение среднеквадратичного отклонения к среднему

def covar(x):
    n = len(x)
    x_bar = mean(x)
    print(x_bar, '   Среднее д/ вариационного ряда ', num_friends_three)
    deviations_x = [x_i - x_bar for x_i in x]   # Отклонение от среднего для х
    print('  ')
    print(deviations_x, '  deviations_x - Отклонение от среднего д/ вариационного ряда " х " ', num_friends_three )
    print('  ')
    coeff_var = [(sqrt((dev_x**2)/(n-1))) for dev_x in deviations_x]
    # print(coeff_var, '  Коэффициент вариации (CVar = (std/n) × 100) для ', num_friends_three)
    return coeff_var
print('  ')
print(covar(num_friends_three), '     ->  ->   CVar (в % ?)  для  ', num_friends_three)


print('  ')
print(' КОВАРИАЦИЯ, КОРЕЛЯЦИЯ  ')
print('  ')
num_friends_three = [100, 49, 41, 40, 25 ]
daily_minutes = [31, 32, 37, 34, 20]


print(num_friends_three, daily_minutes, ' вариационные ряды для Ковариации')

def mean(x_):
    return sum(x_) / len(x_)


print(mean(num_friends_three), ' среднее варриационного ряда')
print('  ')
def de_mean(x_):
    x_bar = mean(x_) # Среднее арифметическое коллекции
    print(x_bar, '   x_bar среднее арифметическое варриационного ряда')
    print('  ')
    return [x_ix - x_bar for x_ix in x_] # среднее результата будет равно нулю
print(de_mean(num_friends_three ), '  отклонение от среднего = варианта минус среднее ')

def variance_for_correlation(x_):  # ДИСПЕРСИЯ Или variance
    n = len(x_)
    deviations = de_mean(x_)
    print(n, ' длинна списка', deviations, ' deviations')
    sum_of_squares = [y_iy**2 for y_iy in deviations] # прокручиваем отклонения и возводим в квадрат
    print('  ')
    print(sum_of_squares, ' квадрат отклонения от среднего')
    print('  ')
    print(sum(sum_of_squares), '       сумма квадратов')
    print('  ')
    variance_su_sq = (sum(sum_of_squares))/(n - 1)
    # print (variance_su_sq,'         ДИСПЕРСИЯ или variance это сумма квадратов отклонений / n - 1' )
    return sum(sum_of_squares)/(n-1)  # возврат вычисленного значения в точку вызова standart_deviations(х)


def standart_deviations(x_):
    return math.sqrt((variance_for_correlation(x_))) # вызов ф-ции variance(x_)
print(standart_deviations(num_friends_three ), '    std со значением дисперсии из  variance(x_)')


def covariance(x_, y_):
    n = len(x_)
    x_bar = mean(x_)
    y_bar = mean(y_)
    print(x_bar, y_bar, '   Среднее д/ вариационных рядов " х " и " у "')
    x_dev = [x_i - x_bar for x_i in x_]   # Отклонение от среднего для х
    y_dev = [y_i - y_bar for y_i in y_]    # Отклонение от среднего для у
    print('  ')
    print(x_dev , y_dev, '  deviations - Отклонение от среднего д/ вариационных рядов " х " и " у "')
    sum_mult = [i * k for i, k in zip(x_dev , y_dev)]
    print('  ')
    return (sum(sum_mult)/(n - 1)) # dot сумма произведений пар x_dev , y_dev

print('  ')
print(covariance(num_friends_three, daily_minutes ), '                  KОВАРИАЦИЯ для x_, y_')

print(num_friends_three, daily_minutes, ' вариационные ряды для Ковариации')

def correlation(x_, y_):
    stdev_x = standart_deviations(x_)
    stdev_y = standart_deviations(y_)
    print(stdev_x, stdev_y, '  standart_deviations for x_,y_')
    print('  ')
    if stdev_x>0 and stdev_y>0 :
        return  covariance(x_, y_)/ stdev_x / stdev_y
    else:
        return 0
print('correlation = ' ,correlation(num_friends_three, daily_minutes))


print(' ')
# Фильтр кореляции от выброса

outlier_index = num_friends_three.index(100)

num_friends_good = [num_friends_three[k] for k,i in enumerate(num_friends_three) if k != outlier_index]
print(num_friends_good, ' удаление выброса из вар ряда num_friends_three')

daily_minutes_good = [ daily_minutes[k] for k,i in enumerate(daily_minutes) if k != outlier_index]
print(daily_minutes_good, ' удаление выброса из вар ряда daily_minutes')

print('correlation = ' ,correlation(num_friends_good, daily_minutes_good), ' Удалили выброс из выборки коэфф увеличился')