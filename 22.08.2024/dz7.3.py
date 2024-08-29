from typing import Optional

def second_index(text: str, some_str: str) -> Optional[int]:
    # Знайти перше входження
    first_index = text.find(some_str)
    
    # Якщо перше входження не знайдено, повернути None
    if first_index == -1:
        return None
    
    # Шукати друге входження
    second_index = text.find(some_str, first_index + len(some_str))
    
    # Якщо друге входження знайдено, повернути його індекс, інакше повернути None
    return second_index if second_index != -1 else None


# Перевірка роботи функції
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')
