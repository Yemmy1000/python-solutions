
employee = str(input("Enter employee name: "))
ID = int(input("Enter employee ID: "))
hrlyR = float(input("Enter hourly rate: "))
hrs = float(input("Enter hours worked: "))
pay = hrlyR * hrs
pay = format(pay, '.2f')

print("Employee: " +employee+'\n'
      +"Employee ID: " +str(ID)+'\n'
      +"Rate: " +str(hrlyR)+'\n'
      +"Hours: " +str(hrs)+'\n'
      +"Rate: " +str(hrlyR)+'\n'
      +"Total Pay: " +str(pay))
