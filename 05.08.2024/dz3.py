def list1(lst):
    n = len(lst)
    if n == 0:
        return [[], []]
    else:
        dis = (n+1) // 2 
        first = lst[:dis]
        second = lst[dis:]
        return [first, second]

print(list1([1, 2, 3, 4, 5, 6])) 
print(list1([1, 2, 3])) 
print(list1([1, 2, 3, 4, 5])) 
print(list1([1] ))
print(list1([] ))
