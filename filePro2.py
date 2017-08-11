import os  #os module contains remove and rename functions.


# remove specified employee from the employee sales file
# display weekly sales information, total sales and commission of a specified employee

# sort the file using  employees' names in alphabetical order



def get_employee_sales():
    name = input("Enter employee's name: ")
    string = name.upper()
    for week in range(1,5): # enter sales for four weeks
        sales = input( "Enter week "+ str(week)+ " sales: ")
        string += ' ' + sales
    return string

def save_employee_sales(emp_sales, emp_sales_file):
    file_obj = open(emp_sales_file, 'a')
    file_obj.write(emp_sales+"\n") # write sales to sales file
    file_obj.close()

def payroll_for_the_month(emp_sales_file):
    file_obj = open(emp_sales_file, 'r')
    payroll_file_obj = open('payroll.txt', 'w') #payroll file
    emp_rec = file_obj.readline()  # read first line 
    while emp_rec != '':  #end of file has not been reached
        emp_rec = emp_rec.rstrip('\n')
        emp_rec_list = emp_rec.split() #create a list of employee sales info
        total_sales = 0.0
        for week in range(1,5):  # add sales
            total_sales += float(emp_rec_list[week])
        if total_sales <= 200: #calculate commission
            commission=total_sales*.05
        elif total_sales >200 and total_sales <=500:
            commission = 200*0.5 + (total_sales-200)*.02
        else:
            commission = 200*.05 + 300*.02 + (total_sales-500)*0.01
        payroll_file_obj.write(emp_rec_list[0] + ' ' +\
                               str(total_sales) + ' ' +\
                               str(commission) + "\n")
        emp_rec = file_obj.readline()
    file_obj.close()
    payroll_file_obj.close()


# search for an employee in the employee sales file
def search_emp(name, emp_sales_file):
    rec_found = False
    fileObj = open(emp_sales_file, 'r')
    emp_rec =fileObj.readlines()
    for rec in range(len(emp_rec)) :
        if name in emp_rec[rec] :
             rec_found = True
    fileObj.close()
    return rec_found


def remove_emp(name, emp_sales_file):
    if search_emp(name, emp_sales_file):
        fileObj = open(emp_sales_file, 'r')
        emp_rec =fileObj.readlines()
        for item in range(len(emp_rec)) :
            if name in emp_rec[item] :
                emp_rec[item] = ""
        fileObj.close()
        fileObj = open(emp_sales_file, 'w')
        fileObj.writelines(emp_rec)
        fileObj.close()
        print("The record of ", name , "successfully removed") 
        

def display_payroll_all():
    file_obj = open('payroll.txt', 'r')
    print(file_obj.read())
    file_obj.close()

def display_payroll_individual(emp_name, emp_sales_file):
    if search_emp(emp_name, emp_sales_file):
        file_obj = open('payroll.txt', 'r')
        fileObj = open(emp_sales_file, 'r')
        sales_rec = fileObj.readlines()
        for item in range(len(sales_rec)) :
            if name in sales_rec[item] :
                emp_sale_rec = sales_rec[item]
        
        payroll_rec = fileObj.readlines()
        for item in range(len(payroll_rec)) :
            if name in payroll_rec[item] :
                emp_payroll_rec = payroll_rec[item]

        file_obj.close()
        fileObj.close()
        print(emp_sale_rec, emp_payroll_rec )


def menu():
    quit = False
    #os.remove('abc_sales.txt') # remove file to start afresh.
    while not quit:
        command = int(input("Enter a code 0-Add, 1-Monthly Payroll, 2-Display, 3-Search, 4-Remove, 5-Quit: "))

        if command == 0:
            string = get_employee_sales()
            save_employee_sales(string, 'abc_sales.txt')
            
        elif command == 1:
            payroll_for_the_month('abc_sales.txt')
            
        elif command == 2:
            command2 = int(input("Enter a code 0-All, 1-Individual: "))
            if command2 == 0 :
                 display_payroll_all()
            elif command2 == 1 :
                name = input("Enter the name of employee to display: ")
                display_payroll_individual(name, 'abc_sales.txt')
            else:
                print('Wrong code')

        elif command == 3:
            name = input("Enter the name of employee to search: ")
            name = name.upper()
            if search_emp(name, 'abc_sales.txt'):
                print("Employee ",name , "is found!")
            else:
                print("Employee: ", name, " is not found")
                
        elif command == 4:
            name = input("Enter the name of employee to remove: ")
            name = name.upper()
            remove_emp(name, 'abc_sales.txt')
            
        elif command == 5:
            quit = True
        else:
            print('Wrong code')

menu()


