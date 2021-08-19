class student:
    data="hello"
    #def __init__(self):default constructor
        #self.name="Anmol"
    def __init__(self,name): #Prameterized constructor
        self.name=name
    def display(self):
        print(student.data)
        print(self.name)
    def __del__(self):#destructor
        cname=self.__class__.__name__
        print(cname,"Class object is deleted")
obj=student("Anmol")#Prameterized constructor argument
student.data="hiiii"#changing the value of attribute
print(student.data)
obj.display()
obj.add="Varanasi"
setattr(obj,"district","varanasi")#creating new attribute in the class
#del student.data deleting data member
print(student.data)
#print(self.name) error field
print(obj.name)
print(obj.district)
obj.display()
    
