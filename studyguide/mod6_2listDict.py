def cumValues(dictobj):
    cumlist = []
    sumitem = 0
    for k,v in dictobj.items():
        for item in v:
            sumitem += item
        cumlist.append(sumitem)
        sumitem =0
    return cumlist

def main():
    print(cumValues({0:[1,0,1], 2:[0,3,4,5], 3:[-1,2,-4]}))

main()
