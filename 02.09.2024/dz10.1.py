from typing import Callable, Generator

def pow(x: int) -> int:
    """Підносить число до квадрату."""
    return x ** 2


def some_gen(begin: int, n: int, func: Callable[[int], int]) -> Generator[int, None, None]:
    """
    Генератор числової послідовності.

    :param begin: Перший елемент послідовності.
    :param n: Кількість елементів у послідовності.
    :param func: Функція, яка формує значення для послідовності.
    :return: Генератор числової послідовності.
    """
    current = begin
    for _ in range(n):
        yield current
        current = func(current)


from inspect import isgenerator

# Створення генератора з початковим значенням 2, кількістю членів 4 та функцією pow
gen = some_gen(2, 4, pow)

# Перевірка, що це генератор
assert isgenerator(gen) == True, 'Test1'

# Перетворення генератора в список і перевірка правильності значень
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')
