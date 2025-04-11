
def main():

    correct_password = "12345"
    

    print("ВВЕДИТЕ ПАРОЛЬ ДЛЯ ВХОДА В ПРОГРАММУ")
    

    attempts_left = 3
    
    while attempts_left > 0:

        entered_password = input("Пароль: ")
        

        if entered_password == correct_password:
            print("ДОБРО ПОЖАЛОВАТЬ!")
            return  
        else:
            attempts_left -= 1  
            
            if attempts_left > 0:
                print(f"ПАРОЛЬ НЕВЕРНЫЙ! ИСПОЛЬЗУЙТЕ ЕЩЕ ОДНУ ПОПЫТКУ ({attempts_left} попыток осталось)")
            else:
                print("ВЫ ПРЕВЫСИЛИ ДОПУСТИМОЕ ЧИСЛО ПОПЫТОК! ДО СВИДАНИЯ!")
                return  

if __name__ == "__main__":
    main()