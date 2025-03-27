import random

# Глобальные параметры
N = 20  # Количество чисел в файле
MIN_VAL = -100  # Минимальное значение случайного числа
MAX_VAL = 100   # Максимальное значение случайного числа

# Шаг 1: Генерация случайных чисел и запись их в файл
with open('random_numbers.txt', 'w') as f:
    for _ in range(N):
        num = str(random.randint(MIN_VAL, MAX_VAL)) + '\n'
        f.write(num)

# Шаг 2: Чтение чисел из файла и подсчет количества пар противоположных чисел
opposite_pairs_count = 0
numbers_set = set()

with open('random_numbers.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        
        # Проверяем наличие противоположного числа
        opposite_number = -number
        if opposite_number in numbers_set:
            opposite_pairs_count += 1
        
        # Добавляем текущее число в набор
        numbers_set.add(number)

# Выводим результат
print(f'Количество пар противоположных чисел: {opposite_pairs_count}')