from math import pi
PL = 0
PL2 = 0
kmh = int(input("Введите массу: "))
ms = int(input("Введите объём: "))
kmh2 = int(input("Введите массу2: "))
ms2 = int(input("Введите объём2: "))
PL = kmh / ms
PL2 = kmh2 / ms2
if PL > PL2:
    print(f"{PL} Плотнасть 1 больше, чем {PL2} Плотнасть 2")
else:
    print(f"{PL2} Плотнасть 2 больше, чем {PL} Плотность 1")