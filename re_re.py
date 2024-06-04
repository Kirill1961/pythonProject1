import datetime
import re
from bs4 import BeautifulSoup

s = 'aC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

res = re.match('AC/DC', s, flags=re.I)  # поиск подстроки В НАЧАЛЕ СТРОКИ s
print(res, res.group(), " res.group()>>>>>>>>", "\n")

res = re.search('/DC', s)  # поиск ВО ВСЕЙ СТРОКЕ и выводит первую попавшуюся подстроку
print(res, " search('/DC', s)", "\n")
print(res[0], "\n")  # что бы вывести без описания пишем так res[0]

res = re.findall('CA', s)  # поиск ПОВСЕЙ СТРОКЕ всех заданных подстрок
print(res, " findall('CA', s)", "\n")

res = re.split('A', s)  # делит строку по заданному разделителю
print(res, " split", "\n")

st = 'что бы! вывести? без Петрова Ё. Е. описания  пишем& так ** res[0]'
# " r " - сырая строка, отключено экранирование
res = re.findall(r'вы', st, flags=re.I)
print(res, " findall res 1", "\n")

st = 'что бы! 15вывести? без Петрова Ё. Е. описание548  пишем& так ** res[0]'
# pattern = r'\w+\s[А-ЯЁа-яё]{1}\.\s*[А-ЯЁа-яё]{1}\.'


res = re.findall(r'(\w+)\s[А-ЯЁа-яё]{1}\.\s*[А-ЯЁа-яё]{1}\.', st)
print(res, " findall res 2", "\n")

res = re.search(r'\d+[а-о]', st)
print(res, " search res 3", "\n")

# Находим и возвращаем одни цифры
s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.findall("\d", s)
print(res, " Находим и возвращаем одни цифры findall( '\d', s) ", "\n")

# sub - самое простое использование re.sub("что надо заменить","чем надо заменить", "строка где надо заменить")
# .
#  больше вариантов применения в док-ции.

pattern = 'aa, "\n"'
s = 'aabb'
result = re.sub(pattern, '>>>>', s)

print(result, " 1й вариант замена pattern на s", "\n")

pattern = 'fg'
s = 'fgbb'
res = re.sub(pattern, '***', s)

print(res, " 2й вариант замена pattern на s", "\n")

phone_no = '(212)-456-7890'
pattern = '\D'  # '\D' - всё кроме цифр меняем в строке
result = re.sub(pattern, '*', phone_no)

print(result, " замена дефисов на  звёздочки", "\n")


# возводим в квадрат цифры в строках, d+ это цифры в строке
def square(match):
    num = int(match.group())  # group() -  возвращает полное совпадение конкретной подгруппы
    print(num, " NUM", "\n")
    return str(num * num)


l = ['A1', 'A2', 'A3']
pattern = r'\d+'  # d это цифры в строках, '+' - это несколько символов d

new_l = [re.sub(pattern, square, s) for s in l]  # re.sub(что, чем, где)

print(new_l, " возводим в квадрат цифры в строках", "\n")


# меняем в строке А на В
# group() - Возвращает одну или несколько подгрупп совпадения
# Через системную переменную match из ОБ re.Match можно выводить методом group() группы
#  если в скобках group() нет числа то возвращается вся группа.
def square(match):
    num = int(match.group())
    return str(num * num)


l = ['A1', 'A2', 'A3']
pattern = r'\D'

new_l = [re.sub(pattern, " B", s) for s in l]

print(new_l, " меняем в строке А на В", "\n")

# group() - Возвращает одну или несколько подгрупп совпадения
# Группа определяется помещением выражения в круглые скобки ().

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)  # The entire match

m.group(1)  # The first parenthesized subgroup.

m.group(2)  # The second parenthesized subgroup.

m.group(1, 2)  # Multiple arguments give us a tuple.

print(m.group())
print(m.group(0))  # в скобках № группы
print(m.group(1))
print(m.group(2))
print(m.group(0, 2))


# Поиск, замена  и возврат  чисел из строки
def func(x):
    print(x, "\n")
    return " 500 "


s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.sub(r"(test_sub) (\d)", func, s)
print(res, " Поиск, замена  и возврат  чисел из строки", "\n")


# Поиск и просто замена чисел в строке
def func(x):
    print(x, "\n")
    return " 500 "


s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.sub(r" (\d)", func, s)
print(res, " Поиск и просто замена чисел в строке", "\n")


# Группа определяется помещением выражения в круглые скобки ()
# в ОБ re.Match группам присваивается порядковый номер (test_sub) - первая, (\d) - вторая.
def func(match):
    print(match.group(2))
    integ = match.group(2)
    return integ


s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.sub(r"(test_sub) (\d)", func, s)
print(res, " Поиск и просто замена чисел в строке", "\n")

# Простушка с опострофом "[a'-z]+" то же самое что (\w+)
i = [['statistic', 'R', 'go', '99', 'numpy', 'MongoDB', 'pandas', 'data science'],
     ['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
     ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
     ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science']
     ]
print("Простушка с опострофом:", "\n")
for i_ in i:
    for ri in i_:
        r = re.findall("[a'-z]+", ri)

        print(r, "\n")

# re со словарём
s = {"id": 1,
     "username": "joelgrus",
     "text": "Is anyone data science  ",
     "created_at": datetime.datetime.now(),
     "liked_by": ["data_gay", "data_gal", "data science", "data science"]
     }


def token(x):
    for i in x.keys():
        # print(x[i])
        tok = re.findall(r"[a-z0-9]+", str(x[i]))  # Вариант без больших букв
        tok_w = re.findall(r"[\W\w]+", str(x[i]))  # Вариант с большими буквами
        yield tok, tok_w


print(list(token(s)), "re со словарём ", "\n")
