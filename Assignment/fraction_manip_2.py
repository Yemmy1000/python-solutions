class Fraction:
    def __init__(self, a,b):
        self.__n = a
        self.__d = b
        
    def __str__(self):
        g = self.gcd(self.__n, self.__d)
        if g != 0:
            n = int(self.__n/g)
            d = int(self.__d/g)
            return str(n) + "/" + str(d)
        else:
            return str(0) + "/" + str(0)
        
    def gcd(self, a,b):
        sign = 1
        if a==0 or b == 0:
            return 0
        if a<0 and b<0:
            a = -a
            b = -b
        if a <0:
            a = -a
            sign = -1
        if b <0:
            b = -b
            sign = -1
 
        if a>=b:
            g = a%b
            if g==0:
                return sign*b
            else:
                return sign*self.gcd(b, g)
        else:
            g = b%a
            if g == 0:
                return sign*a
            else:
                return sign*self.gcd(g, a)
            
    def add(self, f):
        n = self.__n*f.__d + self.__d*f.__n
        d = self.__d*f.__d
        g = self.gcd(n,d)

        if g != 0:
            return Fraction(int(n/g), int(d/g))
        else:
            return Fraction(0,0)
        
    def subtract(self, f):
        n = self.__n*f.__d - self.__d*f.__n
        d = self.__d*f.__d
        g = self.gcd(n,d)
        if g != 0:
            return Fraction(int(n/g), int(d/g))
        else:
            return Fraction(0,0)
        
    def divide(self, f):
        n = self.__n*f.__d
        d = self.__d*f.__n
        g = self.gcd(n,d)
        return Fraction(int(n/g), int(d/g))
    
    def multiply(self, f):
        n = self.__n*f.__n
        d = self.__d*f.__d
        g = self.gcd(n,d)
        return Fraction(int(n/g), int(d/g))
    
    def pow(self, n):
        if n - int(n) != 0:
            print("Oops!, exponent is not integer")
            exit
        else:
            accu = Fraction(self.__n, self.__d)
            nn= n
            if n<0:
                nn = -n
            for i in range(1,nn):
                accu = accu.multiply(Fraction(self.__n, self.__d))
            if n== 0:
                return Fraction(1, 1)
            elif n<0:
                return Fraction(accu.__d,accu.__n)
            return accu

def get_fraction():
    user_input = input("Enter fraction in form of a/b: ")
    frac_lst = user_input.split('/')
    nom, den = int(frac_lst[0]), int(frac_lst[1])
    return nom, den

def frac_obj():
    nomin, denom = get_fraction()
    return Fraction(nomin, denom)

def display(frac):
    print("Fraction")
    

def menu():
    fracObj = Fraction(0,0)
    quit = False
    while not quit:
        command = int(input("\nEnter 0-Quit; 1-Replace Fraction; 2-Add a new Fraction;\n3-Subtract a new Fraction; 4-Multiply a new Fraction; \n5-Divide Fraction; 6-Exponentiation; 7-Print: "))

        if command == 1:    #code=1 for replacing the original Fraction object with a new Fraction object;
            nomin, denom = get_fraction()
            fracObj = Fraction(nomin, denom)
            
        elif command == 2:  #code = 2 for adding a new Fraction to the original object;
            nomin, denom = get_fraction()
            fracObj2 = Fraction(nomin, denom)
            fracObj = fracObj.add(fracObj2)

        elif command == 3:  #code=3 for subtracting a new Fraction from the original object;
            nomin, denom = get_fraction()
            fracObj2 = Fraction(nomin, denom)
            fracObj = fracObj.subtract(fracObj2)
               
        elif command == 4:  #code =4 for multiplying a new Fraction object to the original object;
            nomin, denom = get_fraction()
            fracObj2 = Fraction(nomin, denom)
            fracObj = fracObj.multiply(fracObj2)
            
        elif command == 5:  #code=5 for dividing the original object by a new Fraction object;
            nomin, denom = get_fraction()
            fracObj2 = Fraction(nomin, denom)
            fracObj = fracObj.divide(fracObj2)
            
        elif command == 6:  #code=6 for the nth exponent of the original object;
            nomin, denom = get_fraction()
            fracObj2 = Fraction(nomin, denom)
            fracObj = fracObj.pow(fracObj2)
            
        
        elif command == 7:  #code =7 to print the current value of the original object.
            print(fracObj)
            
            
        elif command == 0:  #quit
            quit = True
            print("\nGoodbye!")
           
    
        else:
            print("Wrong code")

          
  
             
menu()
