class StudentRec:
    def __init__(self, stdrec):
        self.__StdRec = stdrec

    def __str__(self):
        return str(self.__StdRec)



    def addStdRec(self, mat_no, name, dept):
        stdrec_str = matno +"," + name + "," + dept
        self.__StdRec[mat_no] = stdrec_str



def main():
    
    print("===================This application creates Students record============")
    mat_no = input("Enter Student Matric No: ")
    name = input("Enter Student name: ")
    dept = input("Enter Student dept No: ")

    stdrec = (mat_no,name,dept)
    std = StudentRec(stdrec)
    print(std)


main()
