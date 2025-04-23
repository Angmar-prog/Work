n = int(input("Введите натуральное число: "))
if n <= 0:
    print("Число должно быть положительным.")
else:
    max_digit = 0
    min_digit = 9
    while n > 0:
        digit = n % 10  
        max_digit = max(max_digit, digit)
        min_digit = min(min_digit, digit)
        n //= 10  
    print(f"Максимальная цифра: {max_digit}")
    print(f"Минимальная цифра: {min_digit}")