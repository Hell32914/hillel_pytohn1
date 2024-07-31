number = int(input("Enter number: "))

a1 = number // 1000
a2 = (number % 1000) // 100
a3 = (number % 100) // 10
a4 = number % 10

print(a1)
print(a2)
print(a3)
print(a4)
