def obsh(x, y): #  это коммент
    array = []
    for i in range(2, min(x, y)+1):
        if x % i == 0 and y % i == 0:
            array.append(i)
    return array
print(obsh(12, 18))


def chet(x): # определяем функцию с входным параметром х
    if x % 2 == 0: # если число кратно 2ум, то возвращаем тру
        return True
    else: # иначе возвращаем фолз - нечетное
        return False


def simple(x): # проверяем число на простоту( если число делится на 1 и на самого себя)
    count = 0 # обнуляем счетчик делителей
    for i in range(1, x+1): # начинаем перебор от 1 до самого числа
        if x % i == 0: # если исходное число поделилось на переборное, то переборное - это делитель
            count += 1 # увеличиваем счетчик делителей на 1
    if count == 2: # если делителей 2 , то это 1 и само число, значит исходное число простое
        return True # возвращаем тру - простое
    else:
        return False # возвращаем фолз - составное


def ost(x): # функция вывода всех остатков числа
    array = [] # список всех остатков объявляется открытым
    for i in range(1, x+1): # начинаем перебор от 1 до самого числа
        if x % i == 0: # если исходное число поделилось на переборное, то переборное - это делитель
            array.append(i) # теку3щий делитель записываем в список
    return array # возвращаем этот список
