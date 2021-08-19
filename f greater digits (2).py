def greater(num):
    x=1
    while(num!=0):
        mod=num%10
        num=num//10
        if mod>x:
            x=mod
    print(x,"is greater")


num=int(input("enter any number"))
greater(num)





#by itration
num=input("enter any digit number")
x=1
for i in iter(num):
    if int(i)>int(x):
        x=i
print(x,"is greater digit")
