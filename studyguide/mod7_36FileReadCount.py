fname = input("Enter file name to open ")

try:
    fileObj = open(fname, 'r')

except (IOError, ValueError) as err:
    print(err)
    print("File not exist")
else:
    robj = fileObj.read(5)
    fileObj.close()
    print(robj)
