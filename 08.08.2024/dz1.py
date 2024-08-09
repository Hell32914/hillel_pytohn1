list_of_lists = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for numbers in list_of_lists:
    nz = [x for x in numbers if x != 0]
    z = [x for x in numbers if x == 0]
    result = nz + z
    print(result)