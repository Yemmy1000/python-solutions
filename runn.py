from random import randrange, choice
from time import clock

def get_search_list(n):
    end = (2**64)-1
    nset = set()
    for k in range(n):
        nset.update([randrange(1,end)])
    nlist = list(nset)
    nlist.sort()
    return nlist








def main():
    n = int(input("Enter Number n: "))
    search_list = get_search_list(n)
    search_term = choice(search_list)
    time_linear = clock()
    print(do_linear_search(search_list, search_term))
    print("CPU time for linear search = ", clock() - time_binary)

    
    time_binary = clock()
    print(do_binary_search(search_list, search_term))
    print("CPU time for linear search = ", clock() - time_binary)

main()
