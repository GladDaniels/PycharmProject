import random

test_list = ["1", "2", "3", "4", "5", "6"]
print("Пул элементов:", test_list)

num  = int(input("Введите кол-во элементов в новом массиве "))
print(random.choices(test_list, k=num))

a = [2]*23
print(a)