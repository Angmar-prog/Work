n = float(input("Введите число n: "))
k = 1
S = 0
while True:
    S += 1 / k
    if S > n:
        print(f"Первое число, большее n: {S} (при k = {k})")
        break
    k += 1