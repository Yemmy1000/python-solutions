
for i in range(1, 7):

    for i in range(0,i,1):
        print(format(2**i, "4d"), end="  ")
     

    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end="  ") 
    print('\n')   


