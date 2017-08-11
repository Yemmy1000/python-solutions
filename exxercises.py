#Class HashTable is used to create HashTable objects
class HashTable:
    
    def __init__(self, size):
        self.__size = size   # hash table size
        self.__slots = list(range(self.__size))  #list of slots
        self.__data = {}  #use dictionary to represent the table
        #initialize hash table items to None
        for key in self.__slots:
            self.__data[key] = None
            
    #for printing the hash table
    def __str__(self):
        string = "Key\tItems\n___\t____"
        for k,v in self.__data.items():
            string += "\n" + str(k) + "\t" + str(v)
        return string

    #Defines the hash function
    def hashfunction(self, item):
        return item%self.__size
    #Each slot contains a list object
    #This method adds an item to the list
    def put(self, item):
        hash_value = self.hashfunction(item)
        if self.__data[hash_value] == None:
            self.__data[hash_value] = [item]
        else:
            self.__data[hash_value].append(item)

    #The function that allows for indexing of the hash table
    def __getitem__(self,key):
        return self.__data[key]

    #searches the hash table for an item, returns -1 if not found
    #otherwise returns the slot
    def search(self,item):
        hash_value = self.hashfunction(item)
        if self.__getitem__(hash_value) == None:
            return -1
        if item in self.__getitem__(hash_value):
            return hash_value
        else:
            return -1
