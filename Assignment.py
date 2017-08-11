


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


def display_result_heading(): 
   print("Year# \t New Loan Bal \t Interest Paid \t Acc Interest")
   

def display_result(N, loan_bal, int_pay,interest_pay):
    loan_bal = format(loan_bal, '.2f')
    int_pay = format(int_pay, '.2f')
    interest_pay = format( interest_pay, '.2f')
    print(N,'\t', loan_bal,'\t\t', int_pay,'\t\t', interest_pay)


def main():
    quit = False
    while not quit:
        cmd = eval(input("\nEnter 0 to Continue or 1 to quit:  "))
        if cmd == 0:
            print("Let's compute amortization payment of loan!")
            p = get_loan_amount();
            R = get_rate()
            N = get_period()
            cumul_interest = 0
            a = calculate_monthly_payment(p,R,N)

            print("\n Monthly Payments is: ", format(a,'.2f'))
            display_result_heading()

            for i in range(1,N+1):
                interest_pay, pay_bal = calculate_current_balance(p,R,a)
                cumul_interest = cumul_interest + interest_pay

                if i % 12 == 0:
                    Yrno = i//12
                    display_result(Yrno, pay_bal, interest_pay, cumul_interest)
                p = pay_bal
         
        elif cmd == 1:
            quit = True
            print("Quit...")
        else:
            print("Invalid code, try again!")


main()
