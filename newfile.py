f = open("zxcvb.txt")
N = f.readline()
N = int(N)
for i in range(N):
    num1, num2 = f.readline().split("h")
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        print("из ", num2, "и ", num1, "наибольшее - ", num1)
    if num2 > num1:
        print("из ", num2, "и ", num1, "наибольшее - ", num2)
    if num1 == num2:
        print("из ", num2, "и ", num1, "наибольшего нет")
print("Это конец")
