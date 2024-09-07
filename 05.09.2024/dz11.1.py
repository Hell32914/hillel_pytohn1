from typing import Generator

def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Генератор простих чисел до числа end включно.
    
    :param end: верхня межа для простих чисел
    :return: генератор простих чисел
    """
    
    def prime(n: int) -> bool:
        """
        Перевіряє, чи є число простим.
        
        :param n: число для перевірки
        :return: True, якщо число просте, інакше False
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Генератор для простих чисел до end
    for num in range(2, end + 1):
        if prime(num):
            yield num


# Перевірка генератора
from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
