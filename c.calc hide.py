#class creation

class calculation:
    __num1=0
    __num2=0
    def inputdata(self):
        self.__num1=int(input("enter first number"))
        self.__num2=int(input("enter second number"))
    def __addition(self):
        add=self.__num1+self.__num2
        print("sum=",add)
    def __subtraction(self):
        sub=self.__num1-self.__num2
        print("subtraction=",sub)
    def displayresult(self):
        self.__addition()
        self.__subtraction()



# object creation
calc=calculation()
calc.inputdata()
calc.displayresult()
#calc.subtraction()
