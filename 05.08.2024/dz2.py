def cycl(lst):
    if len(lst) > 1:
        a = lst.pop()
        lst.insert(0, a)
    return lst


print(cycl([1,2,3,4,5]))
print(cycl([1]))
print(cycl([]))



