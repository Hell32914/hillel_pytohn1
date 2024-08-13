import string
import keyword



key_word = keyword.kwlist
allowed_chars = string.ascii_lowercase + string.digits + "_"

name = input("Введіть ім'я змінної:")

if name[0].isdigit():
    print("False")
elif any(char.isupper() for char in name):
    print("False")
elif any(char not in allowed_chars for char in name):
    print("Flase")
elif name.count('_') > 1: 
    print ("False")
elif name in key_word: 
    print("False")
else: print(True)