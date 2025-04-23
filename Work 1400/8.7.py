a = float(input("Введите число a (1 < a ≤ 1.5): "))
if not (1 < a <= 1.5):
    print("Число должно быть в диапазоне (1, 1.5].")
else:
    n = 1 
    while True:
        value = 1 + 1 / n
        if value < a:
            print(f"Первое число, меньшее a: {value} (при n = {n})")
            break
        n += 1