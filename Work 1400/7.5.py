n = int(input("Введите количество сотрудников: "))
if n <= 0:
    print("Число должно быть положительным.")
else:
    masses = []
    print("Введите Зарплату сотрудника:")
    for i in range(n):
        mass = float(input(f"Зарплата {i+1}: "))
        masses.append(mass)
    total_mass = sum(masses)
    print(f"Общая Зарплата: {total_mass}")