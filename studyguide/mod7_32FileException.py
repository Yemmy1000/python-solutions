fname = input("Enter file name to open ")

try:
    fileObj = open(fname, 'r')

except (IOError, ValueError) as err:
    print(err)
    writeobj = open(fname, 'w')
    writeobj.write("File is opened in write mode")
    writeobj.close
    print("File is created and open in write mode")
else:
    robj = fileObj.read()
    fileObj.close()
    print(robj)
