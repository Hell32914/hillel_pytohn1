def user_number(number):
    while number > 9:
        product = 1
        while number > 0:
            product *= number % 10
            number //= 10
        number = product
    return number

user_input = int(input("Введіть ціле число: "))

result = user_number(user_input)
print(result)