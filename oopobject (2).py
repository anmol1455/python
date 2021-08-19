class student:
    data="hello"
    def __init__(self,name): #Prameterized constructor
        self.name=name
    def display(self):
        print(student.data)
        print(self.name)
    def __del__(self):#destructor
        cname=self.__class__.__name__
        print(cname,"Class object is deleted")
obj=student("Anmol")#Prameterized constructor argument
obj1=student("Abhinav")
obj.display()
obj1.display()
obj2=obj
print(student.data)
#print(self.name) error field
print(obj.name)
print(obj2.name)
obj2.display()
print(id(obj),id(obj1),id(obj2))

    
