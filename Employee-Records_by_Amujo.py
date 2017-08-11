print("-----> Author          : Amujo Oluyemi E")
print("-----> Matric No       : 16483005")
print("-----> Course of Study : Comp Sc - Information Security")
print("-----> Email           : oluyemiamujo@gmail.com")
print("-----> Phone No        : 07063717176")
print("-----> Program Title   : Employee Record Processing")

def get_employee_data():
   reference_code = input("Enter employee's ref code: ")
   while reference_code.isalpha() :
      try:   
         reference_code = (input("Wrong code! Enter Numeric code as employee's ref code eg. 001: "))
      except ValueError:
         print("Input cannot be parsed as xter")

   ref_code = int(reference_code)
   name = input("Enter employee's name: ")
   marital_status = input("Enter employee's Marital Status (M/S): ")
   while (marital_status not in "MmsS"):
      marital_status = input("Wrong Code Try M/m for married & S/s for single: ")

   monthly_gross_pay = (input("Enter monthly pay: "))
   while monthly_gross_pay.isalpha() :
      try:   
         monthly_gross_pay = (input("Retry! Enter monthly pay in integer or float: "))
      except ValueError:
         print("Input cannot be parsed as xter")

   monthly_gross_pay = float(monthly_gross_pay)
   return ref_code, reference_code, name, marital_status, monthly_gross_pay

def search_employee(code, emp_dict):
   return code in emp_dict

def add_employee(code, employee, emp_dict):
   if not search_employee(code, emp_dict):
      emp_dict[code] = employee
   else:
      print("Employee: ", employee, " is already in the dictionary")

def remove_employee(code, emp_dict):
    if search_employee(code, emp_dict):
       del emp_dict[code]
    else:
       print("Employee code: ", code, " is not found!")

def display_records(emp_dict):
    print("-------------------------------------------------------------------")
    print("Ref Code  Employee Name\tMarital\tMonthly Gross Pay\tMonthly Net Pay")
    print("-------------------------------------------------------------------")
    for code, value in emp_dict.items():
       v = value.split(',')
       print(v[0],'\t',v[1],'\t',v[2],'\t',v[3],'\t',v[4])
          #print(str(code)+" : "+emp_dict[code])

def monthly_net_pay(marital_status, monthly_gross_pay):
   if marital_status == "M" or marital_status == "m":
      net_pay = monthly_gross_pay - (monthly_gross_pay * 0.15) #where tax is 15% of gross pay
      return format(net_pay, '.2f')
   else :
      net_pay = monthly_gross_pay - (monthly_gross_pay * 0.25) #where tax is 25% of gross pay
      return format(net_pay, '.2f')

def menu():
    quit = False
    employee_dict = {}
    while not quit:
          command = int(input('\nEnter a code 0-new,1-search,2-remove, 3-display, 4-quit '))
          if command == 0:
              ref_code, reference_code, name, marital_status, monthly_gross_pay = get_employee_data()
              mont_net_pay = monthly_net_pay(marital_status, monthly_gross_pay)
              employee = reference_code+", "+(name.upper())+", "+(marital_status.upper())+", "+(str(format(monthly_gross_pay,'.2f')))+", "+(str(mont_net_pay))
              add_employee(ref_code, employee, employee_dict)
          elif command == 1:
              ref_code = int(input("Enter reference code: "))
              if search_employee(ref_code, employee_dict):
                  print("Employee: ", employee_dict[ref_code], " is found")
              else:
                  print("Employee: ", ref_code, " is not found")
          elif command == 2:
              ref_code = int(input("Enter reference code: "))
              remove_employee(ref_code, employee_dict)
          elif command == 3:
              display_records(employee_dict)
          elif command == 4:
              quit = True
              print("Goodbye!")
          else:
              print("Wrong code")
           
             
menu()
