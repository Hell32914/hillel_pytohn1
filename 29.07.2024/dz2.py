def reverse_number(num):
    # Витягуємо кожну цифру
    digit1 = num % 10
    num = num // 10
    digit2 = num % 10
    num = num // 10
    digit3 = num % 10
    num = num // 10
    digit4 = num % 10
    num = num // 10
    digit5 = num % 10
    
    # Збираємо нове число у зворотному порядку
    reversed_num = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5
    
    return reversed_num

# Запитуємо число у користувача
user_input = input("Введіть 5-значне число: ")
number = int(user_input)

# Викликаємо функцію та виводимо результат
reversed_number = reverse_number(number)
print("Перевернуте число:", reversed_number)