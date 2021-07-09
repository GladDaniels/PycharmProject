def gray(x):
    sum = 0
    if len(x) != 3:
        return "Вы ввели не трехзначное число! @"
    else:
        sum += int(x[0])
        sum += int(x[1])
        sum += int(x[2])
        return sum

cink = input("Введите любое трёхзначное число ")
print(gray(cink))
