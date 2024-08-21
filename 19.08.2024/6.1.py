import string

def letters_range(input_range):
    letters = string.ascii_letters
    start, end = input_range.split('-')
    start_index = letters.index(start)
    end_index = letters.index(end) + 1
    return letters[start_index:end_index]

user_input = input("Введіть пару: ")

result = letters_range(user_input)
print("Результат:", result)