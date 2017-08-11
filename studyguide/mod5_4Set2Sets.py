def aMod2(sobj):
    sobj2 = set()
    for i in sobj:
        sobj2.add({i%2})
    print(sobj2)
        
def main():
    sobj = {0,1,2,3,4,5,6}
    aMod2(sobj)
main()
    
    
