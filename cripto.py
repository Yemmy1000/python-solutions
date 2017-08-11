def factGen(n):
    fact = 1
    for index in range(1,n+1):
        fact *=index
        yield fact


def main():
    a = int(input("Enter value: "))
    b = factGen(a)
    for i in b:
        print(i)

main()
