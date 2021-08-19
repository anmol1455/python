import numpy as np
arr=np.empty((4,3),dtype=np.int)
arr=np.ones((1,3))
arr=np.zeros((1,2))

arr[0,1]=98
arr=np.arange(1,26)
arr.shape=(5,5)
print(arr)
print(arr.shape)
r=0
for i in arr:
          r+=1
          c=0
          for j in i:
                    c+=1
                    print([r,c],"=",j,end="")
          print()
print(arr.transpose())
print(np.sort(arr))
#print(np.sqrt(arr))



