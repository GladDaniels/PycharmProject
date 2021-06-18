f = open("umbers.txt")
N = int(f.readline())
maxi = 0
for i in range(N):
    num = f.readline()
    num = int(num)
    print(num)
    if num > maxi:
        maxi = num
print("максимум ", maxi)
