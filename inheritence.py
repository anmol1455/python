class A:
    def A_display(self):
        print("hello, i'm class A")
class B(A):#Single level inheritence
    def B_display(self):
        print("hello, i'm class B")
#class C(B):#Multilevel inherience
#        pass
class C:
    def C_display(self):
        print("hello, i'm class C")
#class D(C,A):#multiple inheritence
#   pass
class D(C,B):#Hybrid inheritence
   pass
#obj=B()
obj=D()
obj.A_display()
obj.C_display()
