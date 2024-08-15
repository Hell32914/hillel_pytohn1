import re
import string

name = input("Введіть рядок:  ")

cleaned_string = re.sub(r'[^a-zA-Z\s]', '', name)

words = cleaned_string.split()
formatted_string = ''.join(word.capitalize() for word in words)

hesh = f"#{formatted_string}"

if len(hesh) > 139:
    hesh = hesh[:139]

print(hesh)