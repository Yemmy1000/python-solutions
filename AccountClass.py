class Account: #Super class

    __balance = 0.0
    __account_no = 0
    __cust_dict = {}
    
    def __init__(self, no=0, balance = 0.0):
        self.__account_no = no
        self.__balance = balance

    def __str__(self):
        return "Account Number = " + str(self.__account_no) + "\n" + \
               "Balance = " + str(self.__balance)

    @property
    def account_no(self):
        return self.__account_no
    
    @account_no.setter
    def account_no(self, no):
        self.__account_no = no

    @property  
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, bal):
        self.__balance = bal


    @property  
    def cust_dic(self):
        return self.__cust_dict
    
    @cust_dic.setter
    def cust_dic(self, name):
        cus_str = self.__account_no + "," + name
        self.__cust_dict[self.__account_no]= cus_str

            
    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
        else:
            print("Insufficient Funds")

    def deposit(self, amt):
        if amt >0:
            self.__balance += amt

class Single(Account):
    __customer = ''
    def __init__(self, customer, no, balance):
        Account.__init__(self,no,balance)
        self.__customer = customer

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, cust):
        self.__customer = cust

    def __str__(self):
        return "Customer : " + self.__customer + "\n" +\
               Account.__str__(self)

class Joint(Account):
    __cust_1st = ''
    __cust_2nd = ''

    def __init__(self, cust_1st, cust_2nd, no, balance):
        Account.__init__(self, no, balance)
        self.__cust_1st = cust_1st
        self.__cust_2nd = cust_2nd

    @property
    def cust_1st(self):
        return self.__cust_1st

    @cust_1st.setter
    def cust_1st(self, cust):
        self.__cust_1st =cust
        
    @property
    def cust_2nd(self):
        return self.__cust_2nd
    
    def __str__(self):
        return "Customer 1: " + self.__cust_1st + "\n" +\
               "Customer 2: " + self.__cust_2nd + "\n" + \
               Account.__str__(self)

    @cust_2nd.setter
    def cust_1st(self, cust):
        self.__cust_2nd =cust
    
        
class Savings_Single(Single):
    __interest = 0.0

    def __init__(self, cust1='', no=0, balance = 0.0,apr=0.0):
        Single.__init__(self, cust1, no, balance)
        self.__interest = apr

    @property
    def interest(self):
        return self.__interest

    @interest.setter
    def interest(self, apr):
        self.__interest = apr

    def interest_earned(self):
        earned  = self.__balance*self.__interest/12.0
        self.balance += earned
        return earned
    
class Savings_Joint(Joint):
    __interest = 0.0
    def __init__(self, cust1='', cust2='', no=0, balance = 0.0, apr=0.0):
        Joint.__init__(self, cust1, cust2, no, balance)
        self.__interest = apr

    @property
    def interest(self):
        return self.__interest

    @interest.setter
    def interest(self, apr):
        self.__interest = apr

    def interest_earned(self):
        earned  = self.__balance*self.__interest/12.0
        self.balance += earned
        return earned
    
class Current_Single(Single):
    __overdraft_rate = 25.0


    def __init__(self, cust1='', no=0, balance = 0.0, cust2=''):
        Single.__init__(self, cust1, no, balance)
        Joint.__init__(self, cust1, cust2, no, balance)

    @property
    def overdraft_rate(self):
        return self.__overdraft_rate

    @overdraft_rate.setter
    def overdraft_rate(self, rate):
        self.__overdraft_rate = rate
        
    def withdraw(self, amt):
        if amt > self.balance:
            self.balance -= (amt + self.__overdraft_rate)
        else:
            self.balance  -= amt
    
class Current_Joint(Joint):
    __overdraft_rate = 25.0


    def __init__(self, cust1='', cust2='', no=0, balance = 0.0):
        Joint.__init__(self, cust1, cust2, no, balance)

    @property
    def overdraft_rate(self):
        return self.__overdraft

    @overdraft_rate.setter
    def overdraft_rate(self, rate):
        self.__overdraft_rate = rate
        
    def withdraw(self, amt):
        if amt > self.balance:  #class the Account's getter
            self.balance -= (amt + self.__overdraft_rate)  #Account's setter
        else:
            self.balance  -= amt

def ATM(account_obj):
    quit = False
    if isinstance(account_obj, Account):

        while not quit:
            try:
                command = int(input
                              ("Enter a code: 0=quit, 1=withdraw, 2=deposit, 3=display: "))
            except ValueError as err:
                print(err)
            if command == 0:
                print(account_obj)
                print("Goodbye!")
                quit = True
            elif command == 1:
                try:
                    amt = float(input("Enter amount to withdraw: "))
                except ValueError as err:
                    amt = 0.0
                    print(err)
                account_obj.withdraw(amt)
            elif command == 2:
                try:
                    amt = float(input("Enter amount to deposit: "))
                except ValueError as err:
                    amt = 0.0
                    print(err)
                account_obj.deposit(amt)
            elif command == 3:
                print(account_obj)
            else:
                print("Wrong code")




