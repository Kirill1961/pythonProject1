""" ЦПТ - независимо от исходного распределения случайных величин, распределение их суммы (или среднего) приближается к
    нормальному распределению по мере увеличения числа этих величин.
    Статистические выводы: при построении доверительных интервалов и проверке гипотез для выборочных средних.
    Машинное обучение и анализ данных:ЦПТ объясняет, почему выборочные средние часто распределены нормально
    Финансовые модели:ЦПТ объясняет, почему распределение доходов или потерь часто близко к нормальному.
    Инженерия и контроль качества:
    ЦПТ позволяет использовать нормальные распределения для оценки характеристик продукции и процессов. """
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as stats


# Генерация случайных выборок из распределения
n = 1000  # Количество выборок
k = 50  # Размер каждой выборки

# Генерация выборок из равномерного распределения
samples = np.random.uniform(low=0, high=1, size=(n, k))

# Вычисление средних значений для каждой выборки
sample_means = np.mean(samples, axis=1)

# Построение гистограммы средних значений выборок
plt.hist(sample_means, bins=30, edgecolor='k', alpha=0.7)
plt.title("Гистограмма средних значений выборок")
plt.xlabel("Средние значения")
plt.ylabel("Частота")
# plt.show()


""" ^ - крышка, шляпка, heat. Обозначает параметр оценки, предсказания, predict. """
# Пример данных
# x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Наблюдения (объясняющие переменные)
# y = np.array([1, 3, 2, 5, 4])  # Ответные значения (зависимые переменные)
#
# # Создание модели линейной регрессии
# model = LinearRegression()
# model.fit(x, y)
#
# # Предсказание значений y
# y_hat = model.predict(x)  # Предсказанные значения
#
# # График фактических и предсказанных значений
# plt.scatter(x, y, color='blue', label='Фактические значения')
# plt.plot(x, y_hat, color='red', label='Предсказанные значения')
# plt.xlabel('Наблюдения (x)')
# plt.ylabel('Ответные значения (y)')
# plt.legend()
# # plt.show()
#
# # Вывод коэффициентов регрессии
# print(f'Коэффициент наклона: {model.coef_[0]}')
# print(f'Перехват: {model.intercept_}')


"""Параметры и признаки нормального распределения"""
# Параметры нормального распределения
# mu, sigma = 0, 1  # Среднее и стандартное отклонение
#
# # Создание данных
# data = np.random.normal(mu, sigma, 1000)
#
# # Гистограмма данных
# plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
#
# # Плотность нормального распределения
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = stats.norm.pdf(x, mu, sigma)
# plt.plot(x, p, 'k', linewidth=2)
# title = "Форма: μ = {:.2f},  σ = {:.2f}".format(mu, sigma)
# plt.title(title)
# # plt.show()
#
# # QQ-плот
# stats.probplot(data, dist="norm", plot=plt)
# plt.title("QQ-плот")
# # plt.show()


""" среднее, медиана и мода"""
# Параметры нормального распределения
mu, sigma = 0, 1  # Среднее и стандартное отклонение

# Создание данных
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
y = stats.norm.pdf(x, mu, sigma)
print(x, y)
# Построение графика
plt.plot(x, y)
plt.axvline(mu, color='r', linestyle='--', label='Среднее (μ)')
plt.axvline(np.median(x), color='g', linestyle='-', label='Медиана')
plt.axvline(stats.mode(x)[0], color='b', linestyle='-', label='Мода')
plt.legend()
plt.title('Нормальное распределение')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.show()
