# The nth tetrahedral number is the sum of the first n triangular numbers

def Tetrahedral(n):
    T_n = []
    for i in range(1,n+1):
        T_n.append(i*(i+1)*(i+2) / 6)
    yield T_n
