import numpy as np
'''arr=np.dtype([("b_name","S20"),("a_name","S20"),("price","f4")])
arr=np.array([('python','anmol',800),('java','abhinav',900),('asp.net','akhand',2000)])
print(arr)
li=[]
n=int(input("enter no of terms"))
for i in range(n):
    li.append(input("enter the elements"))
arr=np.array([li])
print(arr)
r=int(input("enter the no of rows"))
c=int(input("enter the no of columns"))
arr=np.empty((r,c))
print("enter no of elements")
for i in range(0,r):
    for j in range(0,c):
        arr[i,j]=input()
print(arr)'''
arr=np.arange(25)
arr.shape=(5,5)
print(arr)
a=np.ones((5,4))
print(a)
ar=np.zeros((4,4))
print(ar)
arr1=np.empty((2,2))
print(arr1)
print(arr1.ndim)
print(arr.transpose())
#arr.reshape(5,5)
b=np.copy(arr)
print(b)
for i in np.nditer(b):
          print(i)
print(arr[...,1])
print(arr[1,...])
print(arr[...,1:3])
print("--------------------")











