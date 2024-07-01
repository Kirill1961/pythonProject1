word = {'w', 't', 'u', 'l', 'f'}
frase = {'futur'}
for w in word:
    for f in frase:
        if w in f:
            print('ok', "\n")

""" Словарь из 2х множеств с генератором"""
print({w: f for w in word for f in frase if w in f}, " Словарь из 2х множеств с генератором", "\n")

""" Словарь из 2х множеств , обмен местами key/value с генератором"""
print({f: [w for w in word if w in f] for f in frase},
      " Словарь из 2х множеств , обмен местами key/value с генератором", "\n")

""" Множество из итерируемого множества, итерировать можно list или tuple """
print({i + 1000 for i in (j ** 2 for j in {1, 2, 3})},
      " Множество из итерируемого множества, итерировать можно list или tuple ", "\n")

print([p for p in [x * 3 for x in (1, 2, 3)]])

for p in [x * 3 for x in (1, 2, 3, 4, 5)]:
    print(p)

for p in (x * 3 for x in (1, 2, 3, 4, 5)):
    print(p)

# dict() mutable in set() and interception
a = {'scikit learn': 1, 'pandas': 2, 'data science': 4, 'Is anyone': 1, 'data_gay': 1, 'data_gal': 1}
b = {'data_gay': 2, 'data_gal': 3, 'data science': 1, 'Is anyone': 2}

print(set(a.keys()).intersection(set(a.keys())), " dict() mutable in set() and interception", "\n")
print(set(a.keys()) & (set(a.keys())), " dict() mutable in set() and '&'", "\n")
