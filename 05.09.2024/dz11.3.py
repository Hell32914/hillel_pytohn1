def is_even(number: int) -> bool:
    """
    Перевіряє, чи є число парним, без використання операцій ділення.

    :param number: ціле число
    :return: True, якщо число парне, False якщо непарне
    """
    return (number & 1) == 0


# Перевірка
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print('Ok')
