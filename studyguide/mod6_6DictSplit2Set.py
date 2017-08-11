def dictToSet(dictObj):
    setkey = set()
    setvalue = set()
    for k,v in dictObj.items():
        setkey.add(k)
        setvalue.add(v)
    print(setkey,'\n',setvalue)

dictObj = {0:45, 1:67, 2:89}
dictToSet(dictObj)
