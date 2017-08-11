def employeeInfo():
    name = str(input("Enter employee name: "))
    refno = int(input("Enter employee Ref No.: "))
    dept = str(input("Enter employee dept: "))
    return name, refno, dept
   
def main():
    emp_name, emp_refno, emp_dept = employeeInfo()
 
    print("Employee: " +emp_name+'\n'
      +"Employee ID: " +str(emp_refno)+'\n'
      +"Rate: " +str(emp_dept))

main()
