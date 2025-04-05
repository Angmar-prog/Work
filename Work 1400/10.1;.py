import random

a = int(input("Введите значение a: "))
k = int(input("Введите значение k: "))
b = int(input("Введите значение b: "))
if k > b:
    k, b = b, k
for _ in range(a):  
    random_float = random.uniform(k, b)  
    print(random_float)