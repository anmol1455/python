x=int(input("enter the number 1"))
y=int(input("enter the number 2"))
def sumt(n,m):#function with argument no return 
    print("sum operation \n")
    sumt=n+m
    print("sum is",sumt)
def subs(n,m):#function with argument with return
    print("substraction operation \n")
    subs=n-m
    print("difference is",subs)#if u write print below return...
                               #print statement will not be executed
    return subs#The return statement does not print out the value it returns
               #when the function is called.
               #It however causes the function to exit or
               #terminate immediately, even if it is not the last statement
               #of the function.
def mult():#function with no argument with return
    print("multiply operation \n since this function is not argumented we have to take \n input of variables inside the function")
    x=int(input("enter the number 1"))
    y=int(input("enter the number 2"))
    multiply=x*y
    print("multiplication is",multiply)#again return will behave like explained
                                       #in bottom comment of file
    return mult
def div():#function with no argument no return
    print("division operation \n since this function is not argumented we have to take \n input of variables inside the function")
    x=int(input("enter the number 1"))
    y=int(input("enter the number 2"))
    divide=x/y
    print("division is",divide)
sumt(x,y)
subs(x,y)
mult()#mult func has no arguments
div()#div function has no arguments too


#any statement inside a function which is written after return will
#not be executed cz print statement immidietly makes cursor out of function
    
