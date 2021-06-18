N = int(input("Введите количество оценок "))
summa = 0
nomistake = True
for i in range(N):
    mark = int(input("Введите оценку "))
    if mark < 1 or mark > 5:
        print("Ты ввел лажу")
        nomistake = False
        break
    else:
        summa += mark # summa = summa + mark
if nomistake: # if flag == True:
    print("Средний балл: ", summa / N)
    print("Твоя оценка в проклятой школе: ", round(summa / N))
