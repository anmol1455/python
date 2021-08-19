x=int(input("enter first number"))
y=int(input("enter second number"))
lcm=1
if x>y:
    greater=x
else:
    greater=y
while(greater%x==0 and greater%y==0):
    #if(greater%x==0 and greater%y==0):
        lcm=greater
        break
        greater=greater+1
print("Lcm=",lcm)
