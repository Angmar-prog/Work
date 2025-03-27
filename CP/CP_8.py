from datetime import datetime

# Список файлов с информацией
files = [
    {"name": "file1.txt", "extension": ".txt", "size": 100, "date_created": "2023-10-01"},
    {"name": "file2.jpg", "extension": ".jpg", "size": 200, "date_created": "2023-09-30"},
    {"name": "file3.pdf", "extension": ".pdf", "size": 300, "date_created": "2023-09-29"}
]

# Функция для преобразования даты в объект datetime
def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

# Сортировка по имени файла (по возрастанию)
sorted_by_name_ascending = sorted(files, key=lambda x: x["name"])

# Сортировка по имени файла (по убыванию)
sorted_by_name_descending = sorted(files, key=lambda x: x["name"], reverse=True)

# Сортировка по расширению (по возрастанию)
sorted_by_extension_ascending = sorted(files, key=lambda x: x["extension"])

# Сортировка по расширению (по убыванию)
sorted_by_extension_descending = sorted(files, key=lambda x: x["extension"], reverse=True)

# Сортировка по размеру (по возрастанию)
sorted_by_size_ascending = sorted(files, key=lambda x: x["size"])

# Сортировка по размеру (по убыванию)
sorted_by_size_descending = sorted(files, key=lambda x: x["size"], reverse=True)

# Сортировка по дате создания (по возрастанию)
sorted_by_date_ascending = sorted(files, key=lambda x: parse_date(x["date_created"]))

# Сортировка по дате создания (по убыванию)
sorted_by_date_descending = sorted(files, key=lambda x: parse_date(x["date_created"]), reverse=True)

# Подсчет общего объема всех файлов
total_size = sum(file["size"] for file in files)

# Вывод результатов
print("Сортировка по имени файла (по возрастанию):")
for file in sorted_by_name_ascending:
    print(file)

print("\nСортировка по имени файла (по убыванию):")
for file in sorted_by_name_descending:
    print(file)

print("\nСортировка по расширению (по возрастанию):")
for file in sorted_by_extension_ascending:
    print(file)

print("\nСортировка по расширению (по убыванию):")
for file in sorted_by_extension_descending:
    print(file)

print("\nСортировка по размеру (по возрастанию):")
for file in sorted_by_size_ascending:
    print(file)

print("\nСортировка по размеру (по убыванию):")
for file in sorted_by_size_descending:
    print(file)

print("\nСортировка по дате создания (по возрастанию):")
for file in sorted_by_date_ascending:
    print(file)

print("\nСортировка по дате создания (по убыванию):")
for file in sorted_by_date_descending:
    print(file)

print(f"\nОбщий объем всех файлов: {total_size} байт")