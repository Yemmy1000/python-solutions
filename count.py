Tr = 0
Tt = 0
l = [2,7,5,4,8,5,0,1,5,6,8,2,0,6]
n = len(l)

while n > 1:
    Tr = n//2
    n = n - Tr
    Tt = Tt + Tr
    if n == 1:
        Tr = 1
        Tt = Tt + Tr
    #print(Tt)    
print(Tt)        
