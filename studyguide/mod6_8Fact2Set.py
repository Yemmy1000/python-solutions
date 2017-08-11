def factorial(n):
    factSet = set()
    num = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            num *= j
        factSet.add(num)
        num = 1
    print(factSet)




