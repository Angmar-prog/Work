from math import pi
kmh = float(input("Введите радиус круга: "))
ms = float(input("Введите сторона квадрата: "))
Sk = pi * ms * ms
Sp = kmh * kmh
if(Sp > Sk):
    print(f"{ms} площадь квадрата больше, чем {kmh} пплощадь круга")
else:
    print(f"{kmh} пплощадь круга больше, чем {ms} площадь квадрата")