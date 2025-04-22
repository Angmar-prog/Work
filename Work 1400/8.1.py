import random
n = int(input("Напиши число: "))
for _ in range(10):
    random_float = random.uniform(n, 0)
    print(random_float)