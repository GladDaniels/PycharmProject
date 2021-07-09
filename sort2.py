import random
from random import randint


def maxi(y):
    buff = 0
    x = y
    for j in range(len(x)):  # пункт б) повторяем n раз
        for i in range(len(x) - 1):  # сравниваем все соседние элементы
            if x[i] < x[i + 1]:  # делаем замену через буфер
                buff = x[i]
                x[i] = x[i + 1]
                x[i + 1] = buff
    return x


def mini(y):
    buff = 0
    x = y
    for j in range(len(x)):  # пункт б) повторяем n раз
        for i in range(len(x) - 1):  # сравниваем все соседние элементы
            if x[i] > x[i + 1]:  # делаем замену через буфер
                buff = x[i]
                x[i] = x[i + 1]
                x[i + 1] = buff
    return x


array = []
num = int(input("ВВЕДИТЕ КОЛИЧЕСТВО ЭЛЕМЕНТОВ В МАССИВЕ"))
for i in range(num):
    array.append(randint(1, 100))

print(array)
print(maxi(array))
print(mini(array))

