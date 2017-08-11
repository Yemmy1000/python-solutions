
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
lst = []
m = int(input("Enter int"))
for i in range(1,m+1):
    lst.append(fact(i))
print(lst)
