import math

class Fraction:
    def __init__(self, a: int, b: int):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        # Спрощення дробу
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        # Множимо чисельники і знаменники
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        # Приводимо до спільного знаменника і додаємо
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        # Приводимо до спільного знаменника і віднімаємо
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other: 'Fraction') -> bool:
        # Порівняння двох дробів
        return self.a == other.a and self.b == other.b

    def __lt__(self, other: 'Fraction') -> bool:
        # Порівняння: менший за
        return self.a * other.b < other.a * self.b

    def __gt__(self, other: 'Fraction') -> bool:
        # Порівняння: більший за
        return self.a * other.b > other.a * self.b

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"


# Тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
# Тут результат дробу буде Fraction(7, 6) після спрощення
assert str(f_c) == 'Fraction: 7, 6', str(f_c)

f_d = f_b * f_a
# Тут результат дробу буде Fraction(6, 18), який спрощується до Fraction(1, 3)
assert str(f_d) == 'Fraction: 1, 3', str(f_d)

f_e = f_a - f_b
# Результат дробу буде Fraction(3, 18), який спрощується до Fraction(1, 6)
assert str(f_e) == 'Fraction: 1, 6', str(f_e)

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
# Fraction(2, 4) спрощується до Fraction(1, 2), а Fraction(3, 6) також спрощується до Fraction(1, 2)
assert f_1 == f_2  # True

print('OK')
