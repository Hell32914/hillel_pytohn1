def common_elements():
    # Кратні 3 
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    
    # Кратні 5
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}
    
    # Перетин 
    common = multiples_of_3 & multiples_of_5
    
    return common

# Перевірка роботи функції
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test1'

print('ОК')