from random import *

def threeRandoms():
    randVal1 = randrange(25, 85)
    randVal2 = randrange(25, 85)
    randVal3 = randrange(25, 85)
    return randVal1, randVal2, randVal3

def main():
    print ("The program generates 3 random figure :",threeRandoms())

main()
