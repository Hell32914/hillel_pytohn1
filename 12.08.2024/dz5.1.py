import string
import keyword
import re



key_word = keyword.kwlist
allowed_chars = string.ascii_lowercase + string.digits + "_"

name = input("Введіть ім'я змінної:")
name2 = re.findall(r'(_)\1+', name)

if name[0].isdigit():
    print("False")
elif any(char.isupper() for char in name):
    print("False")
elif any(char not in allowed_chars for char in name):
    print("Flase")
elif name2 != []:
    print ("False")
elif name in key_word: 
    print("False")
else: print(True)