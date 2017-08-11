def seriesFunct(n):
    for i in range(n+1):
        print(calcSum(i))

def calcSum(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    else:
        return calcSum(i-1) + i

n = int(input("Enter number "))
seriesFunct(n)
