num=int(input("enter any number"))
x=num**2
if num==x%10 or num==x%100 or num==x%1000:
    print("automorphic no.")
else:
    print("not automorphic no.")
