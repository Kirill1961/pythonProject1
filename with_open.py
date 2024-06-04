
print(sum([int(i) for i in open("eek.txt")]))

v = 0
for i in open("eek.txt"):
    v += int(i)
print(v)