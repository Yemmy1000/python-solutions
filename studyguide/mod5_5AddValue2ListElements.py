def addValue(lstobj, intobj):
    newlstobj = []
    for val in lstobj:
        newval = val + intobj
        newlstobj.append(newval)
    return newlstobj

def main():
    lstobj = [1,2,3,4,5]
    intobj = 5
    print(addValue(lstobj, intobj))

main()
