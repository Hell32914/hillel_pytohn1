def add_one(some_list):
    # Поєдную список в один рядок 
    com_str = ''.join(map(str, some_list))
    # Перетворюю рядок назад у число
    com_int = int(com_str)
    res1 = com_int + 1
    # Перетворюю результат назад у список цифр
    return [int(digit) for digit in str(res1)]

number = [1, 2, 3, 4]
result = add_one(number)

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
print(result)