class ANN:
    def __init__(self, x, w, y):
        self.x = x
        self.y = y
        self.w = w

    def __str__(self):
        return "The Input: "+ str(self.x)+'\n' + "The Weight: "+str(self.w)+ "\n" + "The Output: "+str(self.y)
