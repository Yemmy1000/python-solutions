class contact:
    def __init__(self, n = "", addr = "", iage = 0, p_number = ""):
         self.__name = n
         self.__address = addr
         self.__age = iage
         self.__phone_number = p_number


    def __str__(self):
        return "Name: "+self.__name + "\n"+"Address: "+self.__address+"\n"+"Age: "+str(self.__age)+"\n"+"Phone Number: "+self.__phone_number

    #Accessor of the data attributes
    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age
        
    def get_phone_number(self):
        return self.__phone_number

    #Mutator of the data attributes
    def set_auth_name(self, t_name):
        self.__auth_name = t_name
        
    def set_publ_name(self, p_name):
        self.__publ_name = p_name


