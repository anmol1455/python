s=input("enter the valid string")
if(len(s)>=3 and len(s)<=7):
    
    for i in s:
        if(i.isalpha()):
            o=i
    print(o)
    for num in s:
        if(num.isalpha()):
            j=s.index(num)
    d1=s[0:j]
    d2=s[j+1:]
    if(len(d1)>=1 and len(d1)<=3 and len(d2)>=1 and len(d2)<=3):
        print("first number is",d1,"second number is",d2)
        def sum(a,b):
            print("sum is= ",a+b)
        def subs(a,b):
            print("substraction is= ",a-b)
        def mul(a,b):
            print("Multiplication is= ",a*b)
        def div(a,b):
            print("Division is= ",a/b)
    else:
        print("length of numbers is not valid for opration")
        exit()
    if(o=="a"):
        sum(int(d1),int(d2))
    if(o=="s"):
        subs(int(d1),int(d2))
    if(o=="m"):
        mul(int(d1),int(d2))
    if(o=="d"):
        div(int(d1),int(d2))
else:
    print("String length mismatched")
