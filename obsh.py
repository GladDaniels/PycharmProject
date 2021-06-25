def obsh(x, y):
    array = []
    for i in range(2, min(x, y)+1):
        if x % i == 0 and y % i == 0:
            array.append(i)
    return array

print(obsh(12, 18))