fileObj = open('uniabuja.txt', 'w')
fileObj.write("Hello Oluwple\n")
fileObj.write("Welcome to UNIABUJA\n")
fileObj.write("University of choice for many Nigerians\n")
fileObj.close()

fileObj = open('uniabuja.txt', 'r')
varObj = fileObj.read()
fileObj.close()

print(type(varObj))
print(varObj)

fileObj = open('uniabuja.txt', 'r')
print(list(fileObj))

print(list(fileObj))
fileObj.close()


fileObj = open('uniabuja.txt', 'r')
print(tuple(fileObj))

print(tuple(fileObj))
fileObj.close()


fileObj = open('uniabuja.txt', 'r')
varObj = fileObj.readlines()
fileObj.close()
print(type(varObj))

print(varObj)

for item in varObj:
    print(item)
