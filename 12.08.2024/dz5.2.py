while True:
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
            print("Неправильна дія: ділення на нуль")
        else:
            res = a / b 
    else:
        print("Неправильна дія: невідомий оператор")

    if res is not None:
        print("Результат:", res)

    re_work = input("Хочете продовжити роботу? (y/n):  ").strip().lower()
    if re_work != "y":
        print("Закінчення роботи")
        break