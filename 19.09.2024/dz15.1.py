import math

class Rectangle:
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other: 'Rectangle') -> bool:
        # Прямокутники рівні, якщо їх площі однакові
        return math.isclose(self.get_square(), other.get_square())
    
    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        # Площа нового прямокутника = сума площ двох прямокутників
        new_square = self.get_square() + other.get_square()
        
        # Припустимо, що одна зі сторін нового прямокутника буде такою ж як у поточного
        new_width = self.width
        new_height = new_square / new_width  # Висота підбирається, щоб отримати правильну площу
        
        return Rectangle(new_width, new_height)
    
    def __mul__(self, n: int) -> 'Rectangle':
        # Площа нового прямокутника збільшується в n разів
        new_square = self.get_square() * n
        
        # Створюємо новий прямокутник з тією ж пропорцією ширини до висоти
        aspect_ratio = self.width / self.height
        new_width = math.sqrt(new_square * aspect_ratio)
        new_height = new_square / new_width
        
        return Rectangle(new_width, new_height)
    
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, square={self.get_square()})"


# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
