# from turtle import distance
from collections import Counter
import random
import numpy as np

"""  Модель нейросети K-Nearest Neighbors (K N N )  """


# грубый подсчёт большинства голосов
def raw_major__vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]

    print(winner, " winner ,", votes, " словарь; key - МЕТКА : value - ЧИСЛО повторов")
    return winner


print(
    raw_major__vote(["a", "b", "b", "a", "a", "b", "b", "a", "a", "b", "b"]),
    " raw_major__vote",
)


# Отбор по большинству голосов
# от ближайшей метки до самой дальней, чем больше голосов те ближе находится метка
def majority_vote(
    labels,
):  # Большинство голосов, labels - метки в кол-ве по результату голосования
    print(labels[:-1], " labels[:-1]")
    vote_counts = Counter(
        labels
    )  # vote_counts - Словарь, key  - метка : value - кол-во повторов
    winner, winner_count = vote_counts.most_common(1)[
        0
    ]  # список кортежей из vote_counts, берём кортеж с ind [0]
    print(
        winner, winner_count, " кортеж с наибольшим повторением"
    )  # вытаскиваем из кортежа с ind [0]-1е и 2е значение

    # прокрутка кол-ва голосов, count это значение из словаря vote_counts
    # winner_count - это наибольшее число повторов (голосов),  .
    num_winners = len(
        [count for count in vote_counts.values() if count == winner_count]
    )
    print(num_winners, " len")
    if num_winners == 1:  # если один победитель то возвращаем  его
        return winner
    else:
        return majority_vote(
            (labels[:-1])
        )  # если есть одинаковое число голосов,то повторяем но без самого дальнего


# print(majority_vote ([1,1,3,55,61,55,98,4,1,55,41,1,55,55,55]))
print(
    majority_vote(["a", "b", "b", "a", "a", "b", "b", "a", "a", "b", "b"]),
    " победитель",
)


""" Классификатор, метки 'a' и 'b' это класса которым принадлежат данные  random_points """


def create_labled_points(lables_for_points):
    random_points = np.random.random(10)  # случайные данные
    result = [i for i in zip(random_points, lables_for_points)]  #

    return result


print(
    create_labled_points(["a", "b", "b", "a", "a", "b", "b", "a", "a", "b", "b"])
)  # метки "а" и "b" с задаными повторами

print(" ")


def knn_classify(k, labled_points, new_points):

    # by_distanse = sorted(labled_points, key=lambda   point: distance(point, new_points))
    by_distanse = sorted(labled_points)
    print(by_distanse, "by_distanse")
    k_nearset_labels = [label for label in by_distanse[:k]]
    print(" ")
    print(k_nearset_labels, " k_nearset_labels")
    return majority_vote((k_nearset_labels))


print(
    knn_classify(
        2,
        create_labled_points(["a", "b", "b", "a", "a", "b", "b", "a", "a", "b", "b"]),
        [3],
    ),
    ">>>>>",
)


# a = ['a', 'b', 'b']
# l = []
# for k in enumerate(a):
#     l.append (tuple(k))
#     random.shuffle(l)
#     print(l)

# { (i,k) for i in s for k in a}
