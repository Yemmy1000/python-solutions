print("-----> Author          : Amujo Oluyemi E")
print("-----> Matric No       : 16483005")
print("-----> Course of Study : Comp Sc - Information Security")
print("-----> Email           : oluyemiamujo@gmail.com")
print("-----> Phone No        : 07063717176")
print("-----> Program Title   : Loan Computation")



#some functions that perform specific tasks
def get_loan_amount():
    return float(input("Enter Principal Loan: "))

def get_rate():
    r = float(input("Enter Annual Rate: "))
    return r/(12*100)
    
def get_period():
    n = int(input("Enter Period in year: "))
    return n*12

def calculate_monthly_payment(p,R,N):
    return (p * R *( 1 + R ) ** N ) / ( (( 1 + R )** N) - 1) 

def calculate_current_balance(p,R,a):
    int_pay = p * R
    p_balance = p * (1 + R) - a
    return int_pay, p_balance

#prepare the head of table
def display_result_heading(): 
    print("------------------------------------------------------------")
    print("Year# \t New Loan Bal \t Interest Paid \t Acc Interest")
    print("------------------------------------------------------------")

def display_result(N, loan_bal, int_pay,interest_pay):
    loan_bal = format(loan_bal, '.2f')
    int_pay = format(int_pay, '.2f')
    interest_pay = format( interest_pay, '.2f')
    print(N,'\t', loan_bal,'\t\t', int_pay,'\t\t', interest_pay)

#main function to coordinate others
def main():
    quit = False
    #controls system to continue accepting user's input or quit
    while not quit:
        cmd = eval(input("\nEnter 0 to Continue or 1 to quit:  "))
        if cmd == 0:
            print("Let's compute amortization payment of loan!")
            p = get_loan_amount();
            R = get_rate()
            N = get_period()
            cumul_interest = 0
            a = calculate_monthly_payment(p,R,N)

            #prints Monthly payments once
            print("\n Monthly Payments is: ", format(a,'.2f'))
            display_result_heading()

            #loop through number of months to compute inter_pay, pay_bal ...
            for i in range(1,N+1):
                interest_pay, pay_bal = calculate_current_balance(p,R,a)
                cumul_interest += interest_pay
                p = pay_bal

                #group months in 12s to make year.....  
                if i % 12 == 0:
                    Yrno = i//12
                    display_result(Yrno, pay_bal, interest_pay, cumul_interest)
                
            print("------------------------------------------------------------")
               
        elif cmd == 1:
            quit = True
            print("Bye! see you later!")
        else:
            print("Invalid code, try again!")

#main function to be called first by the compiler
main()
