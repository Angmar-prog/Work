import random

k = int(input("Введите значение k: "))
b = int(input("Введите значение b: "))
if k > b:
    k, b = b, k
for _ in range(k, b):
    random_float = random.uniform(k, b)
    print(random_float)