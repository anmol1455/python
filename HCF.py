num1=int(input("enter first number"))
num2=int(input("enter second number"))
x=1
y=1
q=1
while(x<=num1 and y<=num2):
    if(num1%x==0 and num2%y==0):
        print(x)
        q=q*x   
    x=x+1
    y=y+1
print("\n\n",q,"is HCF  of ",num1,"and",num2)
    
  
