#class creation

class calculation:
    num1=0
    num2=0
    def inputdata(self):
        self.num1=int(input("enter first number"))
        self.num2=int(input("enter second number"))
    def addition(self):
        add=self.num1+self.num2
        print("sum=",add)
    def subtraction(self):
        sub=self.num1-self.num2
        print("subtraction=",sub)



# object creation
calc=calculation()
calc.inputdata()
calc.addition()
calc.subtraction()
