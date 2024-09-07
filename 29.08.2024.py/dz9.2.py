from typing import Tuple

def difference(*args: float) -> float:
    """
    Обчислює різницю між максимальним і мінімальним значеннями з переданих аргументів.

    :param args: Будь-яка кількість аргументів типу float.
    :return: Різниця між максимальним і мінімальним значенням, округлена до двох знаків після коми.
    """
    if not args:
        return 0.0
    
    max_value = max(args)
    min_value = min(args)
    
    result = round(max_value - min_value, 2)
    
    return result


# Тестування функції
assert difference(1, 2, 3) == 2.00, 'Test1'
assert difference(5, -5) == 10.00, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.40, 'Test3'
assert difference() == 0.00, 'Test4'

print('OK')






