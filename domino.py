import random
from random import randint

koloda = ["001", [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [1, 1, 0], [1, 2, 0],
          [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0],
          [3, 3, 0], [3, 4, 0], [3, 5, 0], [3, 6, 0], [4, 4, 0], [4, 5, 0], [4, 6, 0], [5, 5, 0], [5, 6, 0],
          [6, 6, 0]] # all pick
print(koloda)
human = []
comp = []
rand = 0
for i in range(7):
    rand = randint(0, 27)
    if koloda[rand][2] != '0':
        while koloda[rand][2] != 0:
            rand = randint(0, 27)
        human.append(koloda[rand])
        koloda[rand][2] = 1
    else:
        human.append(koloda[rand])
        koloda[rand][2] = 1

for i in range(7):
    rand = randint(0, 27)
    if koloda[rand][2] != 0:
        while koloda[rand][2] != 0:
            rand = randint(0, 27)
        comp.append(koloda[rand])
        koloda[rand][2] = 2
    else:
        comp.append(koloda[rand])
        koloda[rand][2] = 2
print(koloda)
print(human)
print(comp)

