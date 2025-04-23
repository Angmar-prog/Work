n = int(input("Введите количество предметов: "))
if n <= 0:
    print("Число должно быть положительным.")
else:
    masses = []
    print("Введите массу каждого предмета:")
    for i in range(n):
        mass = float(input(f"Масса предмета {i+1}: "))
        masses.append(mass)
    total_mass = sum(masses)
    print(f"Общая масса груза: {total_mass}")