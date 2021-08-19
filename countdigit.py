n=int(input("Enter a positive integer:"))
count=0
total=0
rev=0
arm=0
c=n
while n!=0:
    r=n%10
    rev=rev*10+r
    arm=arm+(r*r*r)
    total=total+r
    n=n//10
    count=count+1
    
print("Number of digits are: ",count)
print("sum of digits are: ",total)
print("Number in reverse oredr:",rev)
if arm==c:
    print("no is armstrong")
else:
    print("not armstrong")
