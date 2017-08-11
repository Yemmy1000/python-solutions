from math import *

def circlePoint(radius, arcangle):
    xCoord = radius*cos(arcangle)
    yCoord = radius*sin(arcangle)
    return xCoord, yCoord 

def main():
    radius, arcangle = float(input("Enter radius of a circle: ")), float(input("Enter arcangle of a circle: "))
    x , y = circlePoint(radius, arcangle)
    x,y = format(x, '.4f') , format(y, '.4f')
    
    print("The x and y coordinates of the circle is: " + str(x) + ' , '+ str(y))

main()
