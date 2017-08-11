#This a menu from which the user enters student's information and
# courses taken
#when all courses have been entered, calculate the cumulative
#grade point average and display the transcripts
def menu():
    stdname = input("Enter student's name: ")
    matric = int(input("Enter matric number: "))
    quit = False 
    courseList = [] #list object containing courses, credits and grades
    while not quit: #while there a new courses to enter
        command = int(input("Enter 0=new course or 1=quit: "))

        if command == 0:
            enter_new_course(courseList)
        elif command == 1:
            quit = True
            cgpa, cum_credits = calculate_cgpa(courseList)
            displayTranscripts(stdname, matric, courseList,cum_credits,cgpa)
        else:
            print("Wrong letter!")

#Used to enter the course code, credits and letter grade and append
#to the course list
def enter_new_course(clist):
    
    coursecode = input("Enter the course code (e.g., CSC807): ")
    credit = int(input("Enter the course credits: "))
    grade = input("Enter a grade: ")
    clist.append(coursecode+','+ str(credit)+',' + grade)

#Calculate and return the cumulative grade average and cumulative credits
def calculate_cgpa(clist):
    acc_credits = 0.0
    acc_grade_points = 0.0
    for item in clist:
        course = item.split(',')
        pt = get_grade_point(course[2])
        acc_credits += float(course[1])
        acc_grade_points += pt*float(course[1])
    return acc_grade_points/acc_credits, acc_credits


#Calculate and return the point grade
def get_grade_point(ch):
    if ch=="A":
        return 5.0
    elif ch == "B":
        return 4.0
    elif ch== "C":
        return 3.0
    elif ch == "D":
        return 2.0
    elif ch == "E":
        return 1.0
    elif ch == "F":
        return 0
#Display the transcripts
def displayTranscripts(std, mat, clist,crdts, cgpa):
    print("Name: ", std, "Matric No.:", mat)
    for item in clist:
        print(item)
    print("Credits: ", crdts, "Cummulative Grade Point Average: ",\
          format(cgpa, ".3f"))

menu()
