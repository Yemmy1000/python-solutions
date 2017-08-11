from math import *

class vector:
    __x = 0
    __y = 0

    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y


    def __str__(self):
        return "Vector("+str(self.__x)+ ", "+str(self.__y)+")"
 
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


    def vector_mag(self):
        return sqrt(x*x + y*y)


    def __add__(self, v):
        x = self.__x + v.__x
        y = self.__y + v.__y
        return vector(x,y)

    def __sub__(self, v):
        x = self.__x - v.__x
        y = self.__y - v.__y
        return vector(x,y)

    def angle(self):
        return atan(self.__y/self.__x)

    def rotate(self, t):
        new_x = self.__x * cos(t) + self.__y * sin((t))
        new_y = -(self.__x) * sin(t) + self.__y * cos(t)
        return vector(new_x,new_y)       
        
