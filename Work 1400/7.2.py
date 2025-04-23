
n = int(input("Введите натуральное число n: "))  
a = []
print("Введите 10 вещественных чисел:")
for i in range(10):
    num = float(input(f"a[{i+1}]: "))
    a.append(num)
total_sum = sum(a)
print(f"Сумма всех вещественных чисел: {total_sum}")