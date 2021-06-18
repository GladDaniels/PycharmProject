maximum = 0  # обнулили данные
summa = 0  # обнулили данные
for i in range(5): # повторить 5 раз
    a = input("Введите число") # Внимание, СТРОКА!
    a = int(a) # переводим строку в число
    summa = summa + a # Добавляем в перменную новые числа
    if a > maximum:
        maximum = a
print("Максимум", maximum)
print("Сумма", summa)
