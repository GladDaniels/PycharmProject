def gray(x):
    sum = 0
    for i in range(len(x)):
        if x[i] not in "01234567890":
            return "Вы ввели не число! @"
        else:
            sum += int(x[i])
    return sum

cink = input("Введите любое число ")
print(gray(cink))
