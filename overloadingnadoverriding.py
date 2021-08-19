class A:
    def add(self,a,b):
        c=a+b
        print("sum=",c)
class B(A):
    def add(self,a,b,c):
        d=a+b+c
        print("sum=",d)
obj=B()
obj.add(10,20,30)
