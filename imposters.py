from random import randint
count = 0
for i in range(8):
    k = randint(0, 1)
    if k == 0:
        print("imposter")
        count += 1
    if k == 1:
        print("crewmate")
print("There are ", count, "imposters")
