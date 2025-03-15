class A:
    def __init__(self, number):
        self.number = number
        self.digits = [int(d) for d in str(number)]
    
    def get_max_odd_digit(self):
        """Возвращает максимальную нечётную цифру или None, если их нет"""
        odd_digits = [d for d in self.digits if d % 2 != 0]
        return max(odd_digits) if odd_digits else None
    
    def get_min_digit_position(self):
        """Возвращает позицию минимальной цифры (1-based index)"""
        min_digit = min(self.digits)
        position = self.digits.index(min_digit) + 1  
        return position

# Пример использования:
if __name__ == "__main__":
    num = 345672  
    analyzer = A(num)
    
    max_odd = analyzer.get_max_odd_digit()
    print(f"Максимальная нечётная цифра: {max_odd}")  
    
    min_pos = analyzer.get_min_digit_position()
    print(f"Номер минимальной цифры: {min_pos}")      