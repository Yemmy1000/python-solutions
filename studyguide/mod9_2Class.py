class book:
    def __init__(self, t_name = "", p_name = ""):
        self.__auth_name = t_name
        self.__publ_name = p_name


    def __str__(self):
        return self.__auth_name + ","+self.__publ_name

    #Accessor of the data attributes
    def get_auth_name(self):
        return self.__auth_name
        
    def get_publ_name(self):
        return self.__publ_name

    #Mutator of the data attributes
    def set_auth_name(self, t_name):
        self.__auth_name = t_name
        
    def set_publ_name(self, p_name):
        self.__publ_name = p_name
