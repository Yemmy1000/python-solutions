def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

def main():
    num = int(input("Enter number :"))
    for i in range(1,num+1):
        series = 1 / fact(i)
        i += series
        print (series)
    print("Total value: ", i)

main()
