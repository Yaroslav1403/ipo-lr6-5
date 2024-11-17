"""
Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение
"""

import random

#Создаём список случайных целых чисел от -50 до 50 размером 25 элементов
random_numbers = [random.randint(-50, 50) for _ in range(25)]

#Подсчитываем количество положительных элементов
positive_count = sum(1 for num in random_numbers if num > 0)
#Подсчитываем количество отрицательных элементов
negative_count= sum(1 for num in random_numbers if num < 0)
#Подсчитываем количество нулевых элементов
zero_count = sum(1 for num in random_numbers if num == 0)

#Определяем длину общего количество элементов
all_count = len(random_numbers)

#Вычисление процентов положительных чисел
percent_positive = (positive_count / all_count) * 100
#Вычисление процентов отрицательных чисел
percent_negative = (negative_count / all_count) * 100
#Вычисление процентов нулевых чисел
percent_zero = (zero_count / all_count) * 100

#Находим самое большое значение
max_value = max(random_numbers)
#Находим самое малое значение
min_value = min(random_numbers)

#Выводим результаты
print("Список случайных чисел:", random_numbers)
print("Количество положительных чисел:", positive_count, f"({percent_positive:}%)")
print("Количество отрицательных чисел:", negative_count, f"({percent_negative:}%)")
print("Количество нулевых чисел:", zero_count, f"({percent_zero:}%)")
print("Самое большое значение:", max_value)
print("Самое маленькое значение:", min_value)
