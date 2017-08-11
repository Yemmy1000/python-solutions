
from random import *

def funcRands(n):
    if n < 20:
        for i in range(n):
            print(randrange(5,10))
    else:
        print("Invalid! number greater than 20")

def main():
    n = int(input("Enter number less than 20:"))
    funcRands(n)

main()
