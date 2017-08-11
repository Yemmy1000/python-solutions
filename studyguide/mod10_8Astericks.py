
height= int(input("Enter n" ))
row = 0
count = 0
n = height-height+1
funcTree(n)


def funcTree(n):
    if n == height:
        print("*")
    else:
        for i in range(n):
            print("*")
    funcTree(n+1)  
 

