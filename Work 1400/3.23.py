def transform_number(n):
    if n < 100 or n > 999:
        raise ValueError("Число должно быть трехзначным")
    last_digit = n % 10
    remaining_number = n // 10
    new_number = last_digit * 100 + remaining_number
    return new_number
number = 456
result = transform_number(number)
print(f"Исходное число: {number}, полученное число: {result}")