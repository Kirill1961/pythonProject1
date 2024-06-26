import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

"""геометрическая интерпретация KDE заключается в том, что мы строим "облако"
 гауссовских распределений вокруг каждой точки данных, которые затем суммируются 
 для получения общей оценки плотности вероятности для всей выборки данных."""

# Выборка данных для оценки
# data = np.array([-0.2, -0.1, 0, 0.00001, 0.05, 0.1, 0.2])  # 10 - выброс который увеличивает std
data = [
    -5,
    -4,
    -3,
    -2,
    -1,
    -0.5,
    -0.4,
    -0.3,
    -0.2,
    -0.1,
    0,
    0.00001,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    1,
    2,
    3,
    4,
    5,
]


# Создание оценки плотности вероятности с использованием KDE
kde = gaussian_kde(data)
# print(kde.pdf(data), "PDF")  # вычисление плотности вероятности для всех data
# print(kde.evaluate(0.5), "evaluate")  # оценка вычесленной плотности вероятности для всех data
# print(kde.factor, "bandwidth ")  # bandwidth - ширина ядра /разброс / ширина окна


# Создание точек для вычисления плотности вероятности
x_values = np.linspace(min(data) - 0.1, max(data) + 0.1, 10)

# выборка для вычисления плотности вероятности данных точек
x = [-5.5, 1.5, 2.5, 3.5, 4.1, 5]

# Вычисление плотности вероятности для каждой точки
evaluate_values = kde.evaluate(x)
evaluate_values = kde.evaluate(x)
evaluate_values = kde.evaluate(x)
evaluate_values = kde.evaluate(x)
print(evaluate_values, "evaluate_values")


# Вычисляем значения функции плотности вероятности в этих точках
pdf_values = kde.pdf(x)
print(pdf_values, "pdf_values")


# Построение графика
plt.plot(x, evaluate_values, label="KDE")
plt.hist(data, bins=30, density=True, alpha=0.5, label="Histogram")
plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")
plt.title("Оценка плотности вероятности")
plt.legend()
plt.show()


"""bins: Этот параметр определяет количество столбцов в гистограмме или интервалов, 
на которые будет разделена величина данных"""
data = [0.1, 0.2, 0.3, 0.4, 0.5, 1, 2, 3, 3.1, 3.3, 3.7, 4, 5]

# Построение гистограммы
plt.hist(data, bins=30, density=True, alpha=0.5)

plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")
plt.title("Гистограмма данных")
# plt.show()
