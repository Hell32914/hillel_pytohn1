from typing import List, Union, Optional
from collections import Counter

def find_unique_value(some_list: List[Union[int, float]]) -> Optional[Union[int, float]]:
    # Підраховуємо частоту кожного елемента
    counts = Counter(some_list)
    
    # Знаходимо і повертаємо унікальне число
    for number, count in counts.items():
        if count == 1:
            return number
    
    # У разі, якщо не знайдено унікальних чисел
    return None


# Перевірка роботи функції
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")
