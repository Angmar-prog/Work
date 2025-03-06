class DigitProcessor:
    def __init__(self, number):
        self.number = number
        # Преобразуем число в список цифр
        self.digits = [int(d) for d in str(number)]
    
    def get_max_digit(self):
        """Возвращает максимальную цифру в числе"""
        return max(self.digits)
    
    def get_min_digit(self):
        """Возвращает минимальную цифру в числе"""
        return min(self.digits)

# Пример использования:
if __name__ == "__main__":
    num = DigitProcessor(3468219)
    print("Максимальная цифра:", num.get_max_digit())  # Выведет 9
    print("Минимальная цифра:", num.get_min_digit())   # Выведет 1