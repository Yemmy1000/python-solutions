class SumFunct:

    def __init__(self):
        self.n = 0
        self.funct = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.n +=1
        self.funct += (self.n-1) + (self.n**2)
        return self.funct



