class calculator:
    __total = 0.0
    
    def __init__(self, t = 0):
        self.__total = t

    def __add__(self, s):
        self.__total += s
        return self.__total # displays the current total

    def __sub__(self, s):
        self.__total -= s
        return self.__total  # displays the current total

    def __truediv__(self, s):
        self.__total /= s
        return self.__total

    def __mul__(self, s):  #total = total*s
        self.__total *= s
        return self.__total

    def __mod__(self, s):  # total = total%s
        self.__total %= s
        return self.__total

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, a):
        self.__total = a

    def __str__(self):
        return str(self.__total)


