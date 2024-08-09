import random

x = random.randint(3,10)

random_numbers = [random.randint(3, 10) for _ in range(x)] 

print(random_numbers)

new_list = []
new_list.append(random_numbers[0])
new_list.append(random_numbers[2]) 
new_list.append(random_numbers[-2])

print(new_list)
