def perimetr(x, y):
    x = int(x)
    y = int(y)
    return x * y

def square(x, y):
    x = int(x)
    y = int(y)
    return 2*(x + y)

d = input("Введите ширину ")
g = input("Введите длниу ")
print("периметр равен", perimetr(d, g))
print("периметр равен", square(d, g))