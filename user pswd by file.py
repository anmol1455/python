user=input("input user name")
x=2
#name="jarvis"
#passwd="123456"
file=open("user.txt","rt")
data=file.read().split()
print(data)
while(user!=data[0] and x>0):
    print("you have",x,"attempt")
    print("enter correct username")
    user=input()
    x=x-1

if(user==data[0]):
    passw=input("enter passward")
    while(passw!=data[1] and x>0):
        print("you have",x,"attempt")
        print("enter correct passward")
        passw=input()
        x=x-1
    if(passw==data[1]):
        print("yor are login")
    else:
        print("account blocked")
else:
    print("account blocked")
file.close()
