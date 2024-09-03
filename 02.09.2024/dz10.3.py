def is_even(digit):
    """Перевіряє, чи є число парним."""
    return digit % 2 == 0

# Тестування функції
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
