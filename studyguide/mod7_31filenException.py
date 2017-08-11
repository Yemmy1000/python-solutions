fname = input("Enter file name to open ")

try:
    fileObj = open(fname, 'r')

except (IOError, ValueError) as err:
    print(err)
    robj = "File not found"
else:
    robj = fileObj.read()
    fileObj.close()

print(robj)
