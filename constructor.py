class calc:
          country="india"
          def __init__(self,a,b):
                    self.first=a
                    self.sec=b
                    self.c=self.first+self.sec
                    self.city="varanasi"
                    print("hello i am constructor")
          def dis(self):
                    print("total=",self.c)
                    add="vns"
          def pr(self):
                    print(calc.country)
                    print(self.city)
                    
a=calc(100,500)
a.pr()
print(calc.country)
print(a.city)


                    
