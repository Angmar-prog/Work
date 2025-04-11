def sum_real_numbers():
    n = int(input("Введите количество вещественных чисел: "))
    total_sum = 0.0
    for _ in range(n):
     real_number = float(input("Введите вещественное число: "))
    total_sum += real_number
    return total_sum
result = sum_real_numbers()
print(f"Сумма всех вещественных чисел равна {result}")