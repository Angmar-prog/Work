from math import pi
PL = 0
kmh = int(input("Количество членов: "))
ms = int(input("Первый член: "))
ms2 = int(input("Последний член: "))
PL = kmh / 2 * (ms + ms2)
print(f"{PL} сумма")
