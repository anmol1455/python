class student:
    name=""
    age=0
    rollno=0
    def inputdata(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
        self.rollno=int(input("enter your roll no."))
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
        print("student roll no.:",self.rollno)

#object
stud=student()
stud.inputdata()
stud.display()
