print("-----> Author          : Amujo Oluyemi E")
print("-----> Matric No       : 16483005")
print("-----> Course of Study : Comp Sc - Information Security")
print("-----> Email           : oluyemiamujo@gmail.com")
print("-----> Phone No        : 07063717176")
print("-----> Program Title   : Employee Record Processing")

class student:
       
    def __init__(self, n='', m=0, dpt=''):
        self.__name = n
        self.__identity_no = m
        self.__dept = dpt
        self.__courses = {}
        
    def __str__(self):
        return self.__name + ", " + \
               str(self.__identity_no) + ", " +\
               self.__dept 
    
    
    def get_name(self):
        return self.__name
    
    def get_identity_no(self):
        return self.__identity_no
    
    def get_dept(self):
        return self.__dept
    
    def get_cgpa(self):
        return self.calculate_cgpa()
    
    def set_name(self, n):
        self.__name = n
        
    def set_identity_no(self, m):
        self.__identity_no = m
        
    def set_dept(self, dpt):
        self.__dept = dpt

    def addCourse(self, code, units, grade):
        c_str = code +"," + str(units) +"," + grade
        self.__courses[code] = c_str
        
    def delCourse(self, code):
        del self.__courses[code]

    def getCourse(self, code):
        if code in self.__courses:
            return self.__courses[code]
        else:
            return 'No course found'
        
    def deleteCourses(self):
        self.__courses = {}

    def calculate_cgpa(self):
        accCred = 0.0
        accMult = 0.0
        for code in self.__courses:
            course_str = self.__courses[code]
            course_str_list = course_str.split(',')
            units = float(course_str_list[1])
            accCred += units
            grade = course_str_list[2]
            if grade == 'A':
                accMult += units*5.0
            elif grade == 'B':
                accMult += units*4.0
            elif grade == 'C':
                accMult += units*3.0
            elif grade == 'D':
                accMult += units*2.0
            elif grade == 'E':
                accMult += units*1.0
            elif grade == 'F':
                accMult += units*0.0
        return accCred, accMult, accMult/accCred

        
    def displayCourses(self):
        for code in self.__courses:
            print(self.__courses[code])

    def displayCGPA(self):
        acc_credit, acc_point, cgpa = self.get_cgpa()
        print("Accumulated Credits = ", acc_credit, ",", "Earned Points = ", acc_point)
        print("Grade Point Average = ", cgpa)



def main():
    evelyn = student("Evelyn Samson", 8398774)
    #Prompt user to enter 3 courses or more later, one course at a time. 
    for i in range(3):
        c_code = input("Course Code: ")
        c_credit = int(input("Course Credit: "))
        c_grade = input("Course Grade: ")
        evelyn.addCourse(c_code,c_credit,c_grade)
        evelyn.get_cgpa()
    print(evelyn)
    evelyn.displayCourses()
    evelyn.displayCGPA()
           

main()
