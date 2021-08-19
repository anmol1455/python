class account:
    ac_no=0
    ac_holder_name=""
    def inputdata(self):
        self.ac_no=int(input("enter account number"))
        self.ac_holder_name=input("enter account holder name")
    def displaydata(self):
        print("account number:",self.ac_no)
        print("account holder name:",self.ac_holder_name)

        #first derived class(child class)
class saving(account):
    balance=0
    def inputbalance(self):
        self.balance=float(input("enter initial balance"))
    def balanceinfo(self):
        print("available balance is: rs",self.balance)
    def deposit(self):
        amount=float(input("enter amount to deposit"))
        self.balance=self.balance+amount
        print("amount successfully deposited")
        self.balanceinfo()
    def withdraw(self):
        amount=float(input("enter amount to withdraw"))
        if(self.balance-amount>=1000): 
            self.balance=self.balance-amount
            print("amount successfully withdraw")
            self.balanceinfo()
        else:
            print("insuficient balance")
            


        #secont derived class(child class)
class current(account):
    balance=0
    def inputbalance(self):
        self.balance=float(input("enter initial balance"))
    def balanceinfo(self):
        print("available balance is: rs",self.balance)
    def deposit(self):
        amount=float(input("enter amount to deposit"))
        self.balance=self.balance+amount
        print("amount successfully deposited")
        self.balanceinfo()
    def withdraw(self):
        amount=float(input("enter amount to withdraw"))
        if(self.balance-amount>=5000): 
            self.balance=self.balance-amount
            print("amount successfully withdraw")
            self.balanceinfo()
        else:
            print("insuficient balance")




            #object
sac=saving()
print("input detail of saving account")
sac.inputdata()
sac.inputbalance()
sac.displaydata()
sac.balanceinfo()
sac.deposit()
sac.withdraw()
print("input detail of current account")
cac=current()
cac.inputdata()
cac.inputbalance()
cac.displaydata()
cac.balanceinfo()
cac.deposit()
cac.withdraw()
            
