user=input("input user name")
x=2
name="anmol"
passwd="jarvis"
while(user!=name and x>0):
    print("you have",x,"attempt")
    print("enter correct username")
    user=input()
    x=x-1

if(user==name):
    passw=input("enter passward")
    while(passw!=passwd and x>0):
        print("you have",x,"attempt")
        print("enter correct password")
        passw=input()
        x=x-1
    if(passw==passwd):
        print("yor are logged in")
    else:
        print("account blocked")
else:
    print("account blocked")
