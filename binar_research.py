def b_s(a, i):
    l = 0  # индекс начала списка (СП)
    print(l, "индекс начала списка")
    h = len(a) - 1  # индекс последовательности ОБ, -1 тк индексы начин с НУЛЯ
    print(h, "индексы всего списка")
    while l <= h:  #
        m = int((l + h) / 2)  # индекс ОБ находящ по середине СП
        print(m, "индекс середины списка")
        g = a[
            m
        ]  #  g - ОБ находящийся в середине СП, определили по индексу m середины СП
        if g == i:  #
            return m
        if (
            g > i
        ):  # если ОБ середины СП > заданного для поиска i, то 1й инд премещается в правую половину
            h = m - 1  #
        else:
            l = (
                m + 1
            )  # если ОБ середины СП < заданного для поиска i, то посл-й инд премещается в левую половину
    return None


a = [1, 2, 3, 5, 7, 9, 10, 12, 14, 16, 20, 25, 27, 31, 39, 40, 47, 48]
print(b_s(a, 40))
