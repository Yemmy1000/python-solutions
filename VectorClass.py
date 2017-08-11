import math

class vector:
    __x = 0
    __y = 0

    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

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

    def angle_radii(self):
        if self.__x ==0:
            return math.pi/2.0
        else:
            return math.atan(self.__y/self.__x)

    def angle_deg(self):
        return self.angle_radii()*180/math.pi

    def len(self):
        return math.sqrt(self.__x**2.0 + self.__y**2.0)

    def __add__(self, v):
        x = self.__x + v.__x
        y = self.__y + v.__y
        return vector(x,y)

    def __sub__(self, v):
        x = self.__x - v.__x
        y = self.__y - v.__y
        return vector(x,y)
    
    def __rmul__(self, a):  #multiply by scalar from the right.
        return vector(self.__x*a, self.__y*a)

    def unit(self):
        a = 1.0/self.len()
        return self.__rmul__(a)

    def __mul__(self, v):
        x = self.__x * v.__x
        y = self.__y  * v.__y
        return vector(x,y)

    def __str__(self):
        return str((self.__x, self.__y)) #convert tuple to str

    def __add_vec_sca__(self, a, v):
        x = self.__x + a * v.__x
        y = self.__y + a * v.__y
        return vector(x,y)

    def rotate(self, a):
        new_x = self.__x * math.cos(a) + self.__y * math.sin(a)
        new_y = -(self.__x) * math.sin(a) + self.__y * math.cos(a)
        return vector(new_x,new_y)

    def vec_projection(self, v2):
        x = self.__x - (self.__x * v2.__x / self.__x * self.__x) * v2.__x
        y = self.__y - (self.__y * v2.__y / self.__y * self.__y) * v2.__y
        return vector(x, y)

    def __eq__(self, v):
        if self.__x == v.__x and self.__y == v.__y:
            return True
        else:
            return False

    def __neq__(self, v):
        if self.__x != v.__x and self.__y != v.__y:
            return True
        else:
            return False

    def __ge__(self, v):
        if self.len() > v.len():
            return True
        else:
            return False

    def __le__(self, v):
        if (math.sqrt(self.__x**2.0 + self.__y**2.0)) < (math.sqrt(v.__x**2.0 + v.__y**2.0)):
            return True
        else:
            return False

    def __truediv__(self, a):
        x = self.__x / a
        y = self.__y / a
        return vector(x, y)
