"""Конструкция is True используется для проверки того, является ли значение переменной истинным булевым значением
    и is not True является ли значение переменной ложным
    filter(function, iterable)
    - if x: или if not x: выполнение при условии х  истинно или ложно
    - bool(x) или not bool(x) определение истинности или ложности переменной х """

import numpy as np


a = [2, 51, 14, 142, 17, 89, -1]

print([i for i in a if True], " if True  разрешает итерацию списка")

print([i for i in a if False], " if False  неразрешает итерацию списка")

print([0 if True else 1], " if True в тернарном операторе возвращает 1-е значение ")

print([0 if False else 1], " if False в тернарном операторе возвращает 2-е значение ")

# lambda  определяет заданное число совпадений ОБ

a = 5
b = 5
bo_ol = [a == b for _ in range(5)]
print((bo_ol, " Список из одних True"))
print([i for i in filter(lambda r: not r is False, bo_ol)], " ?? not is False - отрицание наличия False")
print([i for i in filter(lambda r: not r, bo_ol)], " ?? not  - отрицание отсутствия True")
if [i for i in filter(lambda r: not r, bo_ol)] is True:
    print("ok")
else:
    print("no")

# Определяем наличие True / False в словаре оператором IN
# filter передаёт в lambda список bo_ol.
print(True in [r for r in filter(lambda r: r is True, bo_ol)], " фильтруем из списка bo_ol только True")
print(False in [r for r in filter(lambda r: r is True, bo_ol)], " фильтруем из списка bo_ol только False")

# определяем пустой или заполненный список с BOOL
print(bool([i for i in filter(lambda x: x is False, bo_ol)]), " проверка присутствия  False - отсутствует")
print(bool([i for i in filter(lambda x: x is True, bo_ol)]), " проверка присутствия  True - присутствует")


# фильтрация списка содержащего только True по РЕР-8 и мой самопис
quotient = [True, True, True]
if not bool([_ for _ in filter(lambda row: row is False, quotient)]):
    print(" True, по РЕР-8 фильтрация списка содержащего только True")
else:
    print("False, по РЕР-8 фильтрация списка содержащего только True")

if bool([_ for _ in filter(lambda row: row is False, quotient)]) == False:
    print(" True, фильтрация списка содержащего только True, мой самопис")
else:
    print("False, фильтрация списка содержащего только True, мой самопис")

# Истинность просто
a = {'scikit learn': 1, 'pandas': 2, 'data science': 4, 'Is anyone': 1, 'data_gay': 1, 'data_gal': 1}
b = {'data_gay': 2, 'data_gal': 3, 'data science': 1, 'Is anyone': 2}

if a and b:
    print("if - Истинность a and b просто")
if not a and b:
    print("OK")
else:
    print("if not - Истинность a and b просто")


# Истинность для матрицы с any() и  all()
# any() и all() используются для проверки истинности элементов итерируемого объекта (списка, множества, кортежа)
arr_a = np.array([[6, 4, 8], [2, 5, 9]])
arr_b = np.array([[7, 1], [4, 0], [3, 4]])

if arr_b.any():
    print("any() - True если любой из элементов не НОЛЬ")
print(arr_b)
if arr_a.all():
    print("all() - True если все элементы не НОЛЬ")
print(arr_a)

# Истинность для итерируемого ОБ
values = [0, 1, 2, 3]

if any(values):
    print("В списке есть хотя бы один истинный элемент.")
else:
    print("Все элементы в списке ложные.")

if all(values):
    print("Все элементы в списке истинные.")
else:
    print("В списке есть хотя бы один ложный элемент.")

# None, bool, not bool - Простой отбор False и  bool
list_true = [0, 2, [], 5, {}, "good"]
x = 5
l = []
print(list(filter(None, list_true)), "None - Простой отбор False")
print(list(filter(lambda x: bool(x), list_true)), "bool - Простой отбор  True  с bool")
print(list(filter(lambda x: not bool(x), list_true)), "not bool - Простой отбор  false  с not bool")
print(bool(x), ": утверждаем х = 5 - истина ;", not bool(x), ": утверждаем х = 5 - ложь")
print(bool(l), ": утверждаем l = [] - истина ;", not bool(l), ": утверждаем l = [] - ложь")


# Наипростейший sort True / False
a = [2, 0, 50, 0, 0]
print([i for i in a if i], "Наипростейший sort True / False")
print([i for i in a if not i], "Наипростейший sort True / False")
