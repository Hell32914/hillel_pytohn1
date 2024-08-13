import string


punctuation = string.punctuation + ' '

name =(input("Введіть рядок:  "))

title = name.title()

filtered_string = ''.join([char for char in title if char not in punctuation])

hesh = "#" + filtered_string

if len(hesh) > 139:
    lenght = hesh[:139] 
    print(lenght)
else: 
    print(hesh)