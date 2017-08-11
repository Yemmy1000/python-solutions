

room1Width = float(input("Enter Width for Room 1: "))
room1Breadth = float(input("Enter Breadth for Room 1: "))

room1Area = room1Width * room1Width


room2Width = float(input("Enter Width for Room 2: "))
room2Breadth = float(input("Enter Breadth for Room 2: "))

room2Area = room2Width * room2Width

room3Width = float(input("Enter Width for Room 3: "))
room3Breadth = float(input("Enter Breadth for Room 3: "))

room3Area = room3Width * room3Width

totalArea = room1Area + room2Area + room3Area

totalArea = format(totalArea, '.3f')

print('Size of room Room 1: ',room1Width,'m ', ' x ',room1Width,'m' )
print('Size of room Room 2: ',room2Width,'m ', ' x ',room2Width,'m' )
print('Size of room Room 3: ',room3Width,'m ', ' x ',room3Width,'m' )
print('Total area of house is ',totalArea,'sq.m. ')

