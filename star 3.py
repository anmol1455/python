for i in range(1,6,1):
    print()
    for j in range(4,i-1,-1):
        print(" ",end=" ")
    for k in range(0,i,1):
        print("*",end=" ")
    for x in range(0,i-1,1):
        print("*",end=" ")



for i in range(1,6,1):
    print()
    for j in range(4,i-1,-1):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for x in range(2,i+1,1):
        print(x,end=" ")
