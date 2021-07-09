def dabudidabudai(x, y):
    x = int(x)
    y = int(y)
    if x % y == 0:
        return "Введённое вами первое число может поделиться на второе"
    else:
        return "Введённое вами первое число не может поделиться на второе"
x = input("Введите любое число ")
y = input("Введите второе число ")
print(dabudidabudai(x, y))