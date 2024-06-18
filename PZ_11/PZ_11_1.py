#Средствами языка Python сформировать два текстовых файла(.txt),
# содержащий по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вила,
# предварительно выполнив требуемую обработку элементов:
#Содержимое первого файла:
#Чётные элементы:
#Произведение чётных элементов:
#Минимальный элемент:
#Содержимое второго файла:
#Нечётные элементы:
#Количество нечётных элементов:
#Сумма нечётных элементов:


import random

# Генерация случайной последовательности положительных чисел
file1 = [random.randint(1, 100) for _ in range(5)] # создаем список из 5 положительных чисел

# Запись последовательности положительных чисел в файл
with open("file1.txt", "w") as file:
    for number in file1:
        file.write(str(number) + "\n")

# Генерация случайной последовательности отрицательных чисел
file2 = [random.randint(-100, -1) for _ in range(5)] # создаем список из 5 отрицательных чисел

# Запись последовательности отрицательных чисел в файл
with open("file2.txt", "w") as file:
    for number in file2:
        file.write(str(number) + "\n")

# Считываем числа из файлов file1.txt и file2.txt
with open("file1.txt", "r") as file:
    file1 = [int(line.strip()) for line in file]

with open("file2.txt", "r") as file:
    file2 = [int(line.strip()) for line in file]

# Обработка чисел и запись результата в новый файл file3.txt
with open("file3.txt", "w") as file:

    # Четные элементы
    even_elements = [str(num) for num in file1 if num % 2 == 0]
    file.write("Чётные элементы:\n")
    file.write(", ".join(even_elements) + "\n")

    # Произведение четных элементов
    number_even = 1
    for num in file1:
        if num % 2 == 0:
            number_even *= num
    file.write("Произведение четных элементов:\n")
    file.write(str(number_even) + "\n")

    # Минимальный элемент
    min_element = min(file1)
    file.write("Минимальный элемент:\n")
    file.write(str(min_element) + "\n")

    # Нечетные элементы
    odd_elements = [str(num) for num in file2 if num % 2 != 0]
    file.write("Нечётные элементы:\n")
    file.write(", ".join(odd_elements) + "\n")

    # Количество нечетных элементов
    count_odd = len(odd_elements)
    file.write("Количество нечётных элементов:\n")
    file.write(str(count_odd) + "\n")

    # Сумма нечетных элементов
    sum_odd = sum(filter(lambda x: x % 2 != 0, file2))
    file.write("Сумма нечётных элементов:\n")
    file.write(str(sum_odd) + "\n")


