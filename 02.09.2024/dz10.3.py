def is_even(digit: int) -> bool:
    """Перевіряє, чи є число парним без використання ділення."""
    return (digit & 1) == 0

# Тестування функції
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
