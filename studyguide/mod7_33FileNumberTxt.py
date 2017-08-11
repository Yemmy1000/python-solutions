fileObj = open('numberss.txt', 'r')
displayObj = fileObj.readline()
fileObj.close()
print(displayObj)
isum=0
lst = list(displayObj)
lst.remove('\n')

print(lst)
for i in lst:
    isum += int(i)
print ("Total: ", isum)




