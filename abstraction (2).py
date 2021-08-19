class A:
    data="abc"
    __pdata="hi"
    _prodata="good"
    def add(self,a,b):
        c=a+b
        print("sum=",c)
        print(A.data)
        print(A.__pdata)
        print(A._prodata)
class B(A):
    def prin(self):
        print(A.data)
        #print(A.__pdata) gives error cz its prvt
        print(A._prodata)
obj=B()
obj.add(10,29)
obj.prin()
        
