n=5
j=n-n+1

def func(j):
    if j==n:
        return j
    else:
        return func(j+1)


print(func(j))
