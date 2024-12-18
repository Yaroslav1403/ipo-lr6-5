"""
Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение
"""
#Импортируем модуль random для генерации случайных целых чисел от -50 до 50 размером 25 элементов
import random

#Создаём список случайных целых чисел от -50 до 50 размером 25 элементов
random_numbers = [random.randint(-50, 50) for _ in range(25)]

#Инициализируем счётчик, который будет хранить количество положительных чисел
positive_count = 0
#Цикл for проходится по каждому числу в списке random_numbers
for num in random_numbers:  
    #Если число больше нуля
    if num > 0:
        #Счётчик положительных чисел увеличивается на 1
        positive_count += 1
        
#Инициализируем счетчик negative_count, который будет хранить количество отрицательных чисел
negative_count = 0
#Цикл for проходится по каждому числу в списке random_numbers
for num in random_numbers: 
    #Если число меньше нуля
    if num < 0:
        #Счётчик отрицательных чисел увеличивается на 1
        negative_count += 1

#Инициализируем счетчик zero_count, который будет хранить количество нулевых чисел
zero_count = 0
#Цикл for проходится по каждому числу в списке random_numbers
for num in random_numbers: 
    #Если число равно нулю
    if num == 0:
        #Счётчик нулевых чисел увеличивается на 1
        zero_count += 1

#Определяем общее количество элементов в списке random_numbers
all_count = len(random_numbers)

#Вычисляем проценты для положительных чисел
percent_positive = (positive_count / all_count) * 100
#Вычисляем проценты для отрицательных чисел
percent_negative = (negative_count / all_count) * 100
#Вычисляем проценты для нулевых чисел
percent_zero = (zero_count / all_count) * 100

#Находим самое большое значение
max_value = max(random_numbers)
#Находим самое малое значение
min_value = min(random_numbers)

#Выводим список случайных чисел
print("Список случайных чисел:", random_numbers)
#Выводим количество положительных чисел
print("Количество положительных чисел:", positive_count, f"({percent_positive:}%)")
#Выводим количество отрицательных чисел
print("Количество отрицательных чисел:", negative_count, f"({percent_negative:}%)")
#Выводим количество нулевых чисел
print("Количество нулевых чисел:", zero_count, f"({percent_zero:}%)")
#Выводим самое большое значение
print("Самое большое значение:", max_value)
#Выводим самое маленькое значение
print("Самое маленькое значение:", min_value)
