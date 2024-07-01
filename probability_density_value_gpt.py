from scipy.integrate import quad


# Определяем функцию плотности вероятности
def f(x):
    return 2 * x


# Вычисляем вероятность для интервала [0.2, 0.6]
a = 0.2
b = 0.6
probability, _ = quad(f, a, b)

# probability - вероятность нахождения некой случайной величины в заданном интервале
# " _ "  - абсолютная погрешность интегрирования
print("Вероятность попадания в интервал [0.2, 0.6]:", probability)
print(_, "абсолютная погрешность интегрирования")
