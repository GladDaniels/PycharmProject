import random
from random import randint

colour = ['YELLOW', 'RED', 'BLUE', 'GREEN'] # colour

smallB = ['+ 2 cards', 'skip a move'] # small bonus (+ 2 cards / skip a move)
bigB = ['+ 4 cards and skipping the movE', 'choose the coloR'] # big bonus (+ 4 cards and skipping the move / choose the colour)
big = 0
cards1 = []
cards2 = []
for i in range(7):
    big = randint(1, 94)
    if big >= 1 and big <= 72:
        numofcard = str(randint(0, 9))  # number of the card (2-9)
        cards1.append(random.choice(colour) + ' ' + numofcard )
    elif big >=73 and big <=88:
        cards1.append(random.choice(colour) + ' ' + random.choice(smallB))
    elif big >=89 and big <=94:
        cards1.append(random.choice(bigB) + '777')
    big = randint(1, 94)
    if big >= 1 and big <= 72:
        numofcard = str(randint(0, 9))  # number of the card (2-9)
        cards2.append(random.choice(colour) + ' ' + numofcard)
    elif big >= 73 and big <= 88:
        cards2.append(random.choice(colour) + ' ' + random.choice(smallB))
    elif big >= 89 and big <= 94:
        cards2.append(random.choice(bigB) + '777')
print(cards1)
print(cards2)
num = random.randint(0, 6)
print(num)

if cards1[num][0] == "G":
    print("Green")
elif cards1[num][0] == "R":
    print("Red")
elif cards1[num][0] == "B":
    print("Blue")
else:
    print("Yellow")
print(int(cards1[num][-1]))

pair = set()
cards2 = []

# for i in range(7):
#     pair.add(random.randint(0, 7))
#     pair.add(random.choice(colour))
#     print(pair)
#     cards2.append(pair)
#     print(cards2)
#     pair.clear()
# print(cards2)
# num = random.randint(0, 6)
# print(cards2[num][0], cards2[num][1])

