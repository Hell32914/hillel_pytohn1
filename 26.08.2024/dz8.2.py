import string

def is_palindrome(text):
    # Приводимо текст до нижнього регістру
    text = text.lower()
    # Видаляємо всі символи, що не є буквами або цифрами
    text = ''.join(char for char in text if char.isalnum())
    # Порівнюємо текст з його зворотньою версією
    return text == text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")