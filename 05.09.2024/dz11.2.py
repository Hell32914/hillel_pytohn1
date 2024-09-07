def generate_cube_numbers(end: int) -> 'Generator[int, None, None]':
    """
    Генератор кубів чисел, починаючи з 2, до тих пір, поки куб не перевищить значення end.
    
    :param end: максимальне значення куба
    :return: генератор кубів чисел
    """
    num = 2
    while True:
        cube = num ** 3
        if cube >= end:
            return
        yield cube
        num += 1


# Перевірка генератора
from typing import Generator
from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729], '10 у кубі це 1000'
print('Ok')



