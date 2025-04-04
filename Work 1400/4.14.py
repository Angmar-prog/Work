from math import pi
PL = 0
PL2 = 0
kmh = int(input("напряжение на концах участка: "))
ms = int(input("сопротивление участка: "))
kmh2 = int(input("напряжение на концах участка2: "))
ms2 = int(input("сопротивление участка2: "))
PL = kmh / ms
PL2 = kmh2 / ms2
if PL > PL2:
    print(f"{PL} сила тока в 1 кбеле меньше, чем {PL2} сила тока в 2 кбеле")
else:
    print(f"{PL2} сила тока в 2 кбеле меньше, чем {PL} сила тока в 1 кбеле")