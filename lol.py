def p(x):
    if x % 2 == 0:
        return True
    else:
        return False

def j(y):
    array = []
    for i in range(1, y+1):
        if y % i == 0:
            array.append(i)

    return array


def q(y):
    array = []
    for i in range(1, y + 1):
        if y % i == 0:
            array.append(i)
    return len(array)

chislo = int(input("Введите число "))
print(p(chislo))
print(j(chislo))
print(q(chislo))


