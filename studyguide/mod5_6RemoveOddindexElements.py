def removeOdds(lstobj):
    for val in lstobj:
        if lstobj.index(val)%2 != 0:
            lstobj.remove(val)
    return lstobj

def main():
    lstobj = [4,3,8,7,5]
    print(removeOdds(lstobj))

main()
