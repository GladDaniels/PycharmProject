def intu(x):
    sum = 0
    x = x[::-1] # развернули строку
    for i in range(len(x)):
        if x[i] not in "01234567890":
            return "Error Loshara"
        else:
            sum += int(x[i]) * 10**i
    return sum

cink = input("Введите любое число ")
print(intu(cink))
