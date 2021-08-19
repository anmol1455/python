                    #file handling
     #writing data into a file
#filevar=open("hello.txt","w")
#name=input("enter your name: ")
#address=input("enter your address: ")
#filevar.write(name)
#filevar.write("\n")
#filevar.write(address)
#print("write operation successful")
#filevar.close()

     #writing data into a file in append mode
#filevar=open("hello.txt","a")
#filevar.write("\n")
#filevar.write("how are you")
#filevar.write("\n")
#filevar.write("try append mode operation")
#filevar.close()

        #reading 20 character from file
#filevar=open("hello.txt","r")
#data=filevar.read(20)
#filevar.close()
#print("data from file: ",data)

        #reading one line from file
#filevar=open("hello.txt","r")
#data=filevar.readline()
#filevar.close()
#print("data from file: ",data)

        #read complete data from file
filevar=open("hello.txt","r")
print("content of file are: ")
for x in filevar:
    print(x)
filevar.close()
