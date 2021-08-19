print("welcome to SBI ATM")
pin=4321
userpin=int(input("Enter your Pin"))
sb=50000
cb=100000
while True:
    if pin==userpin:
            print("Welcome" "Please choose")
            print("1. Withdraw")
            print("2. Balance enquiry")
            print("3. Pin change")
            print("4. Mini Statement")
            print("5. Exit")
    else:print("wrong password")

    userinput=int(input())
   
    if userinput==1:
            print("Choose account for withdraw")
            print("1. Saving account")
            print("2. Current account")

            userinput1=int(input())
            if userinput1==1:
                withdraw=int(input("enter the amount to withdraw from your saving account"))
            if withdraw<=sb:
                print("Your remaining balance is",sb-withdraw)
            else:print("insufficent balance")

            if userinput1==2:
                withdraw=int(input("enter the amount to withdraw from your current account"))
            if withdraw<=cb:
                print("Your remaining balance is",cb-withdraw)
            else:print("insufficent balance")

    elif userinput==2:
            print("Choose which account balance you want to see")
            print("1. Saving account")
            print("2. Current account")
            userinput1=int(input())
            if userinput1==1:
                print("Your account balance",sb)
            elif userinput1==2:
                print("Your account balance",cb)
    elif userinput==3:
    
        newpin=int(input("enter your new pin"))
        pin==newpin
        print(pin)

    elif userinput==4:
        print("select the account of which mini statement you want to see")
        print("1. Saving account")
        print("2. Current account")
        userinput1=int(input())
        if userinput1==1:
            print("your last transaction was")
        if userinput1==2:
            print("Your last transaction was")
    elif userinput==5:
        print("Thank you for visiting us")
        quit()
    print("yes/no")
    res=input()
    if res=="No":
        break;

