def difference(*args: float) -> float:

    # Перевірка на наявність аргументів
    if not args:
        return 0.0
    
    # Знаходження максимального та мінімального значень
    max_value = max(args)
    min_value = min(args)
    
    # Обчислення різниці та округлення до двох знаків після коми
    result = round(max_value - min_value, 2)
    
    return result

assert difference(1, 2, 3) == 2.00, 'Test1'
assert difference(5, -5) == 10.00, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.40, 'Test3'
assert difference() == 0.00, 'Test4'

print('OK')
