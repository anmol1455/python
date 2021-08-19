import numpy as np
'''arr1=np.array([[1,2],[3,4]])
arr2=np.array([[11,12],[15,16]])#array broadcasting
print(arr1)
print(arr2)
print(np.add(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))
print(np.mod(arr1,arr2))
'''
arr=np.arange(25)
arr.shape=(5,5)
print(arr)
print(arr[4])
print(arr[:15])

#print(arr.ndslice(2,10,2))
print(arr[...,1])
print(arr[1,...])
print(arr[...,1:3])
print("--------------------")

print(arr[[0,4,2],[1,0,3]])
for i in np.nditer(arr,order="F"):
          print(i)
          
print(linespace(5,10,5))
