a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = input("Введіть дію (+, -, *, /): ")

res = None 

if c == "+":
    res = a + b 
elif c == "-":
    res = a - b 
elif c == "*":
    res = a * b 
elif c == "/":
    if b == 0:
        print("Неправильна дія")
    else:
        res = a / b 
else:
    print("Неправильна дія")
if res is not None:
    print( res )
