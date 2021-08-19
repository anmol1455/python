import numpy as np
arr=np.arange(45).reshape(3,3,5)
print(arr)
print(arr.shape)
print(arr.ndim)
se=int(input("enter search element"))
r=0
for i in arr:
          r+=1
          c=0
          for j in i:
                    c+=1
                    d=0
                    for k in j:
                        d+=1
                        #print([r,d],"=",k,end="")
                        if([r,d]==se):
                            print("element found")
                        else:
                            print("not found")
                    print()

          
#print(arr.transpose())
#print(np.sort(arr))
#print(np.sqrt(arr))
