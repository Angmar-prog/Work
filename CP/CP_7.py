def find_word_lengths(text):
    # Разбиваем строку на отдельные слова
    words = text.split()
    
    # Инициализируем минимальную и максимальную длины словами из списка
    min_length = len(words[0])
    max_length = len(words[0])
    
    for word in words:
        length = len(word)
        
        # Обновляем минимальную длину, если нашли слово короче
        if length < min_length:
            min_length = length
            
        # Обновляем максимальную длину, если нашли слово длиннее
        if length > max_length:
            max_length = length
    
    return min_length, max_length

# Пример использования
text = "Python is a great programming language"
min_len, max_len = find_word_lengths(text)
print(f"Длина самого короткого слова: {min_len}")
print(f"Длина самого длинного слова: {max_len}")